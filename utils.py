from collections import defaultdict
from sklearn.metrics import precision_recall_fscore_support

def filter_outer_ene_spans(spans):
    ene_spans = [s for s in spans if s["label"].startswith("ENE-")]#any(lbl.startswith("ENE-") for lbl in s["label"])]
    other_spans = [s for s in spans if not s["label"].startswith("ENE-")]#not any(lbl.startswith("ENE-") for lbl in s["label"])]

    # Garder uniquement les ENE-* qui ne contiennent pas d'autres ENE-*
    filtered_ene = []
    for i, s1 in enumerate(ene_spans):
        s1_range = (s1["start"], s1["end"])
        contains_other = False
        for j, s2 in enumerate(ene_spans):
            if i == j:
                continue
            s2_range = (s2["start"], s2["end"])
            if s1_range[0] <= s2_range[0] and s2_range[1] <= s1_range[1]:
                contains_other = True
                break
        if not contains_other:
            filtered_ene.append(s1)

    return other_spans + filtered_ene


def get_token_labels(annotations):
    token_labels = defaultdict(set)
    for ann in annotations:
        start = ann['token_start']
        end = ann['token_end']
        label = ann.get('label') or ann.get('labels')[0]
        for i in range(start, end + 1):
            token_labels[i].add(label)
    return token_labels

def accumulate_labels(gold_docs, pred_docs):
    all_gold = defaultdict(set)
    all_pred = defaultdict(set)
    offset = 0

    for gold, pred in zip(gold_docs, pred_docs):
        gold_labels = get_token_labels(gold)
        pred_labels = get_token_labels(pred)
        token_indices = set(gold_labels.keys()) | set(pred_labels.keys())

        for t in token_indices:
            all_gold[t + offset].update(gold_labels[t])
            all_pred[t + offset].update(pred_labels[t])

        offset += max(token_indices, default=0) + 1

    return all_gold, all_pred

def evaluate_multilabel_token_dataset(gold_docs, pred_docs):
    all_gold, all_pred = accumulate_labels(gold_docs, pred_docs)
    all_tokens = sorted(set(all_gold.keys()) | set(all_pred.keys()))
    all_labels = sorted(set.union(*all_gold.values(), *all_pred.values()))

    y_true = []
    y_pred = []

    for t in all_tokens:
        y_true.append([int(label in all_gold[t]) for label in all_labels])
        y_pred.append([int(label in all_pred[t]) for label in all_labels])

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average=None, labels=range(len(all_labels)), zero_division=0
    )

    macro_p, macro_r, macro_f, _ = precision_recall_fscore_support(
        y_true, y_pred, average='macro', zero_division=0
    )
    micro_p, micro_r, micro_f, _ = precision_recall_fscore_support(
        y_true, y_pred, average='micro', zero_division=0
    )

    results = {
        'per_label': {
            all_labels[i]: {
                'precision': round(precision[i], 3),
                'recall': round(recall[i], 3),
                'f1': round(f1[i], 3)
            } for i in range(len(all_labels))
        },
        'macro_avg': {
            'precision': round(macro_p, 3),
            'recall': round(macro_r, 3),
            'f1': round(macro_f, 3)
        },
        'micro_avg': {
            'precision': round(micro_p, 3),
            'recall': round(micro_r, 3),
            'f1': round(micro_f, 3)
        }
    }

    return results
