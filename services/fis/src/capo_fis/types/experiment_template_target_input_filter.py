"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetInputFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_target_filter_path
    import capo_fis.types.experiment_template_target_filter_values


class ExperimentTemplateTargetInputFilter(TypedDict, closed=True):
    path: "capo_fis.types.experiment_template_target_filter_path.ExperimentTemplateTargetFilterPath"
    """<p>The attribute path for the filter.</p>"""
    values: "capo_fis.types.experiment_template_target_filter_values.ExperimentTemplateTargetFilterValues"
    """<p>The attribute values for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateTargetInputFilter) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    import capo_fis.types.experiment_template_target_filter_values

    out["values"] = (
        capo_fis.types.experiment_template_target_filter_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExperimentTemplateTargetInputFilter:
    out: ExperimentTemplateTargetInputFilter = {}  # type: ignore[typeddict-item]
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("values") is not None:
        import capo_fis.types.experiment_template_target_filter_values

        out["values"] = (
            capo_fis.types.experiment_template_target_filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
