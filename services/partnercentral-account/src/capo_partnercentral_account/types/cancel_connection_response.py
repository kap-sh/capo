"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CancelConnectionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.aws_account_id
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_arn
    import capo_partnercentral_account.types.connection_id
    import capo_partnercentral_account.types.connection_type_detail_map
    import capo_partnercentral_account.types.date_time


class CancelConnectionResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection was canceled.</p>"""
    id: "capo_partnercentral_account.types.connection_id.ConnectionId"
    """<p>The unique identifier of the canceled connection.</p>"""
    arn: "capo_partnercentral_account.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the canceled connection.</p>"""
    other_participant_account_id: (
        "capo_partnercentral_account.types.aws_account_id.AwsAccountId"
    )
    """<p>The AWS account ID of the other participant in the canceled connection.</p>"""
    updated_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection was last updated (canceled).</p>"""
    connection_types: "capo_partnercentral_account.types.connection_type_detail_map.ConnectionTypeDetailMap"
    """<p>The list of connection types that were active before cancellation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelConnectionResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    out["OtherParticipantAccountId"] = value["other_participant_account_id"]
    import capo_partnercentral_account.types.date_time

    out["UpdatedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    import capo_partnercentral_account.types.connection_type_detail_map

    out["ConnectionTypes"] = (
        capo_partnercentral_account.types.connection_type_detail_map.serialize_aws_json_1_0(
            value["connection_types"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelConnectionResponse:
    out: CancelConnectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("OtherParticipantAccountId") is not None:
        out["other_participant_account_id"] = data["OtherParticipantAccountId"]
    else:
        out["other_participant_account_id"] = ""
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["updated_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("ConnectionTypes") is not None:
        import capo_partnercentral_account.types.connection_type_detail_map

        out["connection_types"] = (
            capo_partnercentral_account.types.connection_type_detail_map.deserialize_aws_json_1_0(
                data["ConnectionTypes"]
            )
        )
    else:
        out["connection_types"] = {}
    return out


def redact_sensitive(value: CancelConnectionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_types" in value:
        import capo_partnercentral_account.types.connection_type_detail_map

        out["connection_types"] = (
            capo_partnercentral_account.types.connection_type_detail_map.redact_sensitive(
                value["connection_types"]
            )
        )
    return out
