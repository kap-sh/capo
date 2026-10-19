"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQuerySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.intermediate_table_output_configuration
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.protected_query_status
    import capo_cleanrooms.types.receiver_configurations_list
    import capo_cleanrooms.types.uuid


class ProtectedQuerySummary(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID of the protected query.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the membership that initiated the protected query.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership that initiated the protected query.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the protected query was created.</p>"""
    status: "capo_cleanrooms.types.protected_query_status.ProtectedQueryStatus"
    """<p>The status of the protected query.</p>"""
    receiver_configurations: (
        "capo_cleanrooms.types.receiver_configurations_list.ReceiverConfigurationsList"
    )
    """<p> The receiver configuration.</p>"""
    query_compute_payer_account_id: NotRequired[
        "capo_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the query compute costs.</p>"""
    intermediate_table_configuration: NotRequired[
        "capo_cleanrooms.types.intermediate_table_output_configuration.IntermediateTableOutputConfiguration"
    ]
    """<p>The intermediate table configuration, present when the protected query was triggered by a populate operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQuerySummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    out["status"] = value["status"]
    import capo_cleanrooms.types.receiver_configurations_list

    out["receiverConfigurations"] = (
        capo_cleanrooms.types.receiver_configurations_list.serialize_json(
            value.get("receiver_configurations", [])
        )
    )
    if "query_compute_payer_account_id" in value:
        out["queryComputePayerAccountId"] = value["query_compute_payer_account_id"]
    if "intermediate_table_configuration" in value:
        import capo_cleanrooms.types.intermediate_table_output_configuration

        out["intermediateTableConfiguration"] = (
            capo_cleanrooms.types.intermediate_table_output_configuration.serialize_json(
                value["intermediate_table_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProtectedQuerySummary:
    out: ProtectedQuerySummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        out["membership_arn"] = ""
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("receiverConfigurations") is not None:
        import capo_cleanrooms.types.receiver_configurations_list

        out["receiver_configurations"] = (
            capo_cleanrooms.types.receiver_configurations_list.deserialize_json(
                data["receiverConfigurations"]
            )
        )
    else:
        out["receiver_configurations"] = []
    if data.get("queryComputePayerAccountId") is not None:
        out["query_compute_payer_account_id"] = data["queryComputePayerAccountId"]
    if data.get("intermediateTableConfiguration") is not None:
        import capo_cleanrooms.types.intermediate_table_output_configuration

        out["intermediate_table_configuration"] = (
            capo_cleanrooms.types.intermediate_table_output_configuration.deserialize_json(
                data["intermediateTableConfiguration"]
            )
        )
    return out
