"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationResolvedSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_source
    import capo_connect.types.evaluation_item_resolution_status
    import capo_connect.types.evaluation_resolved_source_value_list


class EvaluationResolvedSource(TypedDict, closed=True):
    source: "capo_connect.types.evaluation_form_item_enablement_source.EvaluationFormItemEnablementSource"
    """<p>The external source, such as contact data, evaluation metadata, form metadata, or AI metrics.</p>"""
    status: "capo_connect.types.evaluation_item_resolution_status.EvaluationItemResolutionStatus"
    """<p>The status of resolving the source. Valid values:</p> <ul> <li> <p> <code>PENDING</code> - The source has not been resolved yet.</p> </li> <li> <p> <code>RESOLVED</code> - The source has been resolved.</p> </li> <li> <p> <code>FAILED</code> - The source could not be resolved.</p> </li> </ul>"""
    values: NotRequired[
        "capo_connect.types.evaluation_resolved_source_value_list.EvaluationResolvedSourceValueList"
    ]
    """<p>The resolved values of the source. Present when <code>Status</code> is <code>RESOLVED</code>. Contains one value for a single-valued source, any number of values for a multi-valued source, and no values when the source is not present on the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationResolvedSource) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_item_enablement_source

    out["Source"] = (
        capo_connect.types.evaluation_form_item_enablement_source.serialize_json(
            value["source"]
        )
    )
    import capo_connect.types.evaluation_item_resolution_status

    out["Status"] = capo_connect.types.evaluation_item_resolution_status.serialize_json(
        value["status"]
    )
    if "values" in value:
        import capo_connect.types.evaluation_resolved_source_value_list

        out["Values"] = (
            capo_connect.types.evaluation_resolved_source_value_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationResolvedSource:
    out: EvaluationResolvedSource = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        import capo_connect.types.evaluation_form_item_enablement_source

        out["source"] = (
            capo_connect.types.evaluation_form_item_enablement_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError("EvaluationResolvedSource.source required")
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_item_resolution_status

        out["status"] = (
            capo_connect.types.evaluation_item_resolution_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_item_resolution_status.EvaluationItemResolutionStatus",
            "",
        )
    if data.get("Values") is not None:
        import capo_connect.types.evaluation_resolved_source_value_list

        out["values"] = (
            capo_connect.types.evaluation_resolved_source_value_list.deserialize_json(
                data["Values"]
            )
        )
    return out
