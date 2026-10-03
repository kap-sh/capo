"""Generated from Smithy shape ``com.amazonaws.glue#FindMatchesMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_importance_list
    import capo_glue.types.confusion_matrix
    import capo_glue.types.generic_bounded_double


class FindMatchesMetrics(TypedDict, closed=True):
    area_under_pr_curve: NotRequired[
        "capo_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The area under the precision/recall curve (AUPRC) is a single number measuring the overall quality of the transform, that is independent of the choice made for precision vs. recall. Higher values indicate that you have a more attractive precision vs. recall tradeoff.</p> <p>For more information, see <a href="https://en.wikipedia.org/wiki/Precision_and_recall">Precision and recall</a> in Wikipedia.</p>"""
    precision: NotRequired[
        "capo_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The precision metric indicates when often your transform is correct when it predicts a match. Specifically, it measures how well the transform finds true positives from the total true positives possible.</p> <p>For more information, see <a href="https://en.wikipedia.org/wiki/Precision_and_recall">Precision and recall</a> in Wikipedia.</p>"""
    recall: NotRequired["capo_glue.types.generic_bounded_double.GenericBoundedDouble"]
    """<p>The recall metric indicates that for an actual match, how often your transform predicts the match. Specifically, it measures how well the transform finds true positives from the total records in the source data.</p> <p>For more information, see <a href="https://en.wikipedia.org/wiki/Precision_and_recall">Precision and recall</a> in Wikipedia.</p>"""
    f1: NotRequired["capo_glue.types.generic_bounded_double.GenericBoundedDouble"]
    """<p>The maximum F1 metric indicates the transform's accuracy between 0 and 1, where 1 is the best accuracy.</p> <p>For more information, see <a href="https://en.wikipedia.org/wiki/F1_score">F1 score</a> in Wikipedia.</p>"""
    confusion_matrix: NotRequired["capo_glue.types.confusion_matrix.ConfusionMatrix"]
    """<p>The confusion matrix shows you what your transform is predicting accurately and what types of errors it is making.</p> <p>For more information, see <a href="https://en.wikipedia.org/wiki/Confusion_matrix">Confusion matrix</a> in Wikipedia.</p>"""
    column_importances: NotRequired[
        "capo_glue.types.column_importance_list.ColumnImportanceList"
    ]
    """<p>A list of <code>ColumnImportance</code> structures containing column importance metrics, sorted in order of descending importance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindMatchesMetrics) -> dict:
    out: dict = {}
    if "area_under_pr_curve" in value:
        out["AreaUnderPRCurve"] = (
            "NaN"
            if value["area_under_pr_curve"] != value["area_under_pr_curve"]
            else "Infinity"
            if value["area_under_pr_curve"] == float("inf")
            else "-Infinity"
            if value["area_under_pr_curve"] == float("-inf")
            else value["area_under_pr_curve"]
        )
    if "precision" in value:
        out["Precision"] = (
            "NaN"
            if value["precision"] != value["precision"]
            else "Infinity"
            if value["precision"] == float("inf")
            else "-Infinity"
            if value["precision"] == float("-inf")
            else value["precision"]
        )
    if "recall" in value:
        out["Recall"] = (
            "NaN"
            if value["recall"] != value["recall"]
            else "Infinity"
            if value["recall"] == float("inf")
            else "-Infinity"
            if value["recall"] == float("-inf")
            else value["recall"]
        )
    if "f1" in value:
        out["F1"] = (
            "NaN"
            if value["f1"] != value["f1"]
            else "Infinity"
            if value["f1"] == float("inf")
            else "-Infinity"
            if value["f1"] == float("-inf")
            else value["f1"]
        )
    if "confusion_matrix" in value:
        import capo_glue.types.confusion_matrix

        out["ConfusionMatrix"] = (
            capo_glue.types.confusion_matrix.serialize_aws_json_1_1(
                value["confusion_matrix"]
            )
        )
    if "column_importances" in value:
        import capo_glue.types.column_importance_list

        out["ColumnImportances"] = (
            capo_glue.types.column_importance_list.serialize_aws_json_1_1(
                value["column_importances"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FindMatchesMetrics:
    out: FindMatchesMetrics = {}  # type: ignore[typeddict-item]
    if data.get("AreaUnderPRCurve") is not None:
        out["area_under_pr_curve"] = float(data["AreaUnderPRCurve"])
    if data.get("Precision") is not None:
        out["precision"] = float(data["Precision"])
    if data.get("Recall") is not None:
        out["recall"] = float(data["Recall"])
    if data.get("F1") is not None:
        out["f1"] = float(data["F1"])
    if data.get("ConfusionMatrix") is not None:
        import capo_glue.types.confusion_matrix

        out["confusion_matrix"] = (
            capo_glue.types.confusion_matrix.deserialize_aws_json_1_1(
                data["ConfusionMatrix"]
            )
        )
    if data.get("ColumnImportances") is not None:
        import capo_glue.types.column_importance_list

        out["column_importances"] = (
            capo_glue.types.column_importance_list.deserialize_aws_json_1_1(
                data["ColumnImportances"]
            )
        )
    return out
