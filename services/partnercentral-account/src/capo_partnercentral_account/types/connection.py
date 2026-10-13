"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#Connection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.aws_account_id
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_arn
    import capo_partnercentral_account.types.connection_id
    import capo_partnercentral_account.types.connection_type_detail_map
    import capo_partnercentral_account.types.date_time


class Connection(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier that the connection belongs to.</p>"""
    id: "capo_partnercentral_account.types.connection_id.ConnectionId"
    """<p>The unique identifier of the connection.</p>"""
    arn: "capo_partnercentral_account.types.connection_arn.ConnectionArn"
    """<p>The AWS Resource Name (ARN) of the connection.</p>"""
    other_participant_account_id: (
        "capo_partnercentral_account.types.aws_account_id.AwsAccountId"
    )
    """<p>The AWS account ID of the other participant in the connection.</p>"""
    updated_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection was last updated.</p>"""
    connection_types: "capo_partnercentral_account.types.connection_type_detail_map.ConnectionTypeDetailMap"
    """<p>The type of connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Connection) -> dict:
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


def deserialize_aws_json_1_0(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("Connection.catalog required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Connection.id required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Connection.arn required")
    if data.get("OtherParticipantAccountId") is not None:
        out["other_participant_account_id"] = data["OtherParticipantAccountId"]
    else:
        raise DeserializationError("Connection.other_participant_account_id required")
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["updated_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError("Connection.updated_at required")
    if data.get("ConnectionTypes") is not None:
        import capo_partnercentral_account.types.connection_type_detail_map

        out["connection_types"] = (
            capo_partnercentral_account.types.connection_type_detail_map.deserialize_aws_json_1_0(
                data["ConnectionTypes"]
            )
        )
    else:
        raise DeserializationError("Connection.connection_types required")
    return out


def redact_sensitive(value: Connection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_types" in value:
        import capo_partnercentral_account.types.connection_type_detail_map

        out["connection_types"] = (
            capo_partnercentral_account.types.connection_type_detail_map.redact_sensitive(
                value["connection_types"]
            )
        )
    return out
