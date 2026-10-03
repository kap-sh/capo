"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_identifier
    import capo_securityhub.types.boolean
    import capo_securityhub.types.finding_history_update_source
    import capo_securityhub.types.finding_history_updates_list
    import capo_securityhub.types.next_token
    import capo_securityhub.types.timestamp


class FindingHistoryRecord(TypedDict, closed=True):
    finding_identifier: NotRequired[
        "capo_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
    ]
    update_time: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> A timestamp that indicates when Security Hub CSPM processed the updated finding record.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    finding_created: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Identifies whether the event marks the creation of a new finding. A value of <code>True</code> means that the finding is newly created. A value of <code>False</code> means that the finding isn’t newly created. </p>"""
    update_source: NotRequired[
        "capo_securityhub.types.finding_history_update_source.FindingHistoryUpdateSource"
    ]
    """<p> Identifies the source of the event that changed the finding. For example, an integrated Amazon Web Services service or third-party partner integration may call <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html"> <code>BatchImportFindings</code> </a>, or an Security Hub CSPM customer may call <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html"> <code>BatchUpdateFindings</code> </a>. </p>"""
    updates: NotRequired[
        "capo_securityhub.types.finding_history_updates_list.FindingHistoryUpdatesList"
    ]
    """<p> An array of objects that provides details about the finding change event, including the Amazon Web Services Security Finding Format (ASFF) field that changed, the value of the field before the change, and the value of the field after the change. </p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p> A token for pagination purposes. Provide this token in the subsequent request to <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsHistory.html"> <code>GetFindingsHistory</code> </a> to get up to an additional 100 results of history for the same finding that you specified in your initial request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryRecord) -> dict:
    out: dict = {}
    if "finding_identifier" in value:
        import capo_securityhub.types.aws_security_finding_identifier

        out["FindingIdentifier"] = (
            capo_securityhub.types.aws_security_finding_identifier.serialize_json(
                value["finding_identifier"]
            )
        )
    if "update_time" in value:
        import capo_securityhub.types.timestamp

        out["UpdateTime"] = capo_securityhub.types.timestamp.serialize_json(
            value["update_time"]
        )
    if "finding_created" in value:
        out["FindingCreated"] = value["finding_created"]
    if "update_source" in value:
        import capo_securityhub.types.finding_history_update_source

        out["UpdateSource"] = (
            capo_securityhub.types.finding_history_update_source.serialize_json(
                value["update_source"]
            )
        )
    if "updates" in value:
        import capo_securityhub.types.finding_history_updates_list

        out["Updates"] = (
            capo_securityhub.types.finding_history_updates_list.serialize_json(
                value["updates"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> FindingHistoryRecord:
    out: FindingHistoryRecord = {}  # type: ignore[typeddict-item]
    if data.get("FindingIdentifier") is not None:
        import capo_securityhub.types.aws_security_finding_identifier

        out["finding_identifier"] = (
            capo_securityhub.types.aws_security_finding_identifier.deserialize_json(
                data["FindingIdentifier"]
            )
        )
    if data.get("UpdateTime") is not None:
        import capo_securityhub.types.timestamp

        out["update_time"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    if data.get("FindingCreated") is not None:
        out["finding_created"] = data["FindingCreated"]
    if data.get("UpdateSource") is not None:
        import capo_securityhub.types.finding_history_update_source

        out["update_source"] = (
            capo_securityhub.types.finding_history_update_source.deserialize_json(
                data["UpdateSource"]
            )
        )
    if data.get("Updates") is not None:
        import capo_securityhub.types.finding_history_updates_list

        out["updates"] = (
            capo_securityhub.types.finding_history_updates_list.deserialize_json(
                data["Updates"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
