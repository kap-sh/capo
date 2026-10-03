"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AdvancedFieldSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.operator
    import capo_cloudtrail.types.selector_field


class AdvancedFieldSelector(TypedDict, closed=True):
    field: "capo_cloudtrail.types.selector_field.SelectorField"
    """<p> A field in a CloudTrail event record on which to filter events to be logged. For event data stores for CloudTrail Insights events, Config configuration items, Audit Manager evidence, or events outside of Amazon Web Services, the field is used only for selecting events as filtering is not supported.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html">AdvancedFieldSelector</a> in the <i>CloudTrail API Reference</i>.</p> <note> <p>Selectors don't support the use of wildcards like <code>*</code> . To match multiple values with a single condition, you may use <code>StartsWith</code>, <code>EndsWith</code>, <code>NotStartsWith</code>, or <code>NotEndsWith</code> to explicitly match the beginning or end of the event field.</p> </note>"""
    equals: NotRequired["capo_cloudtrail.types.operator.Operator"]
    """<p> An operator that includes events that match the exact value of the event record field specified as the value of <code>Field</code>. This is the only valid operator that you can use with the <code>readOnly</code>, <code>eventCategory</code>, and <code>resources.type</code> fields.</p>"""
    starts_with: NotRequired["capo_cloudtrail.types.operator.Operator"]
    """<p>An operator that includes events that match the first few characters of the event record field specified as the value of <code>Field</code>.</p>"""
    ends_with: NotRequired["capo_cloudtrail.types.operator.Operator"]
    """<p>An operator that includes events that match the last few characters of the event record field specified as the value of <code>Field</code>.</p>"""
    not_equals: NotRequired["capo_cloudtrail.types.operator.Operator"]
    """<p> An operator that excludes events that match the exact value of the event record field specified as the value of <code>Field</code>. </p>"""
    not_starts_with: NotRequired["capo_cloudtrail.types.operator.Operator"]
    """<p> An operator that excludes events that match the first few characters of the event record field specified as the value of <code>Field</code>. </p>"""
    not_ends_with: NotRequired["capo_cloudtrail.types.operator.Operator"]
    """<p> An operator that excludes events that match the last few characters of the event record field specified as the value of <code>Field</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedFieldSelector) -> dict:
    out: dict = {}
    out["Field"] = value["field"]
    if "equals" in value:
        import capo_cloudtrail.types.operator

        out["Equals"] = capo_cloudtrail.types.operator.serialize_aws_json_1_1(
            value["equals"]
        )
    if "starts_with" in value:
        import capo_cloudtrail.types.operator

        out["StartsWith"] = capo_cloudtrail.types.operator.serialize_aws_json_1_1(
            value["starts_with"]
        )
    if "ends_with" in value:
        import capo_cloudtrail.types.operator

        out["EndsWith"] = capo_cloudtrail.types.operator.serialize_aws_json_1_1(
            value["ends_with"]
        )
    if "not_equals" in value:
        import capo_cloudtrail.types.operator

        out["NotEquals"] = capo_cloudtrail.types.operator.serialize_aws_json_1_1(
            value["not_equals"]
        )
    if "not_starts_with" in value:
        import capo_cloudtrail.types.operator

        out["NotStartsWith"] = capo_cloudtrail.types.operator.serialize_aws_json_1_1(
            value["not_starts_with"]
        )
    if "not_ends_with" in value:
        import capo_cloudtrail.types.operator

        out["NotEndsWith"] = capo_cloudtrail.types.operator.serialize_aws_json_1_1(
            value["not_ends_with"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdvancedFieldSelector:
    out: AdvancedFieldSelector = {}  # type: ignore[typeddict-item]
    if data.get("Field") is not None:
        out["field"] = data["Field"]
    else:
        raise DeserializationError("AdvancedFieldSelector.field required")
    if data.get("Equals") is not None:
        import capo_cloudtrail.types.operator

        out["equals"] = capo_cloudtrail.types.operator.deserialize_aws_json_1_1(
            data["Equals"]
        )
    if data.get("StartsWith") is not None:
        import capo_cloudtrail.types.operator

        out["starts_with"] = capo_cloudtrail.types.operator.deserialize_aws_json_1_1(
            data["StartsWith"]
        )
    if data.get("EndsWith") is not None:
        import capo_cloudtrail.types.operator

        out["ends_with"] = capo_cloudtrail.types.operator.deserialize_aws_json_1_1(
            data["EndsWith"]
        )
    if data.get("NotEquals") is not None:
        import capo_cloudtrail.types.operator

        out["not_equals"] = capo_cloudtrail.types.operator.deserialize_aws_json_1_1(
            data["NotEquals"]
        )
    if data.get("NotStartsWith") is not None:
        import capo_cloudtrail.types.operator

        out["not_starts_with"] = (
            capo_cloudtrail.types.operator.deserialize_aws_json_1_1(
                data["NotStartsWith"]
            )
        )
    if data.get("NotEndsWith") is not None:
        import capo_cloudtrail.types.operator

        out["not_ends_with"] = capo_cloudtrail.types.operator.deserialize_aws_json_1_1(
            data["NotEndsWith"]
        )
    return out
