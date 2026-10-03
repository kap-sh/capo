"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryUpdateSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.finding_history_update_source_type
    import capo_securityhub.types.non_empty_string


class FindingHistoryUpdateSource(TypedDict, closed=True):
    type: NotRequired[
        "capo_securityhub.types.finding_history_update_source_type.FindingHistoryUpdateSourceType"
    ]
    """<p> Describes the type of finding change event, such as a call to <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html"> <code>BatchImportFindings</code> </a> (by an integrated Amazon Web Services service or third party partner integration) or <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html"> <code>BatchUpdateFindings</code> </a> (by a Security Hub CSPM customer). </p>"""
    identity: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The identity of the source that initiated the finding change event. For example, the Amazon Resource Name (ARN) of a partner that calls BatchImportFindings or of a customer that calls BatchUpdateFindings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryUpdateSource) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_securityhub.types.finding_history_update_source_type

        out["Type"] = (
            capo_securityhub.types.finding_history_update_source_type.serialize_json(
                value["type"]
            )
        )
    if "identity" in value:
        out["Identity"] = value["identity"]
    return out


def deserialize_json(data: dict) -> FindingHistoryUpdateSource:
    out: FindingHistoryUpdateSource = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_securityhub.types.finding_history_update_source_type

        out["type"] = (
            capo_securityhub.types.finding_history_update_source_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("Identity") is not None:
        out["identity"] = data["Identity"]
    return out
