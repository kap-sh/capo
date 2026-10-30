"""Generated from Smithy shape ``com.amazonaws.opensearch#DivergentField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.diff_field_path
    import capo_opensearch.types.diff_field_policy
    import capo_opensearch.types.diff_field_value


class DivergentField(TypedDict, closed=True):
    path: NotRequired["capo_opensearch.types.diff_field_path.DiffFieldPath"]
    """<p>The location of the field within the item.</p>"""
    source_value: NotRequired["capo_opensearch.types.diff_field_value.DiffFieldValue"]
    """<p>The field's value on the source domain.</p>"""
    target_value: NotRequired["capo_opensearch.types.diff_field_value.DiffFieldValue"]
    """<p>The field's value on the target domain.</p>"""
    policy: NotRequired["capo_opensearch.types.diff_field_policy.DiffFieldPolicy"]
    """<p>How the comparison treats this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DivergentField) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "source_value" in value:
        out["SourceValue"] = value["source_value"]
    if "target_value" in value:
        out["TargetValue"] = value["target_value"]
    if "policy" in value:
        import capo_opensearch.types.diff_field_policy

        out["Policy"] = capo_opensearch.types.diff_field_policy.serialize_json(
            value["policy"]
        )
    return out


def deserialize_json(data: dict) -> DivergentField:
    out: DivergentField = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("SourceValue") is not None:
        out["source_value"] = data["SourceValue"]
    if data.get("TargetValue") is not None:
        out["target_value"] = data["TargetValue"]
    if data.get("Policy") is not None:
        import capo_opensearch.types.diff_field_policy

        out["policy"] = capo_opensearch.types.diff_field_policy.deserialize_json(
            data["Policy"]
        )
    return out
