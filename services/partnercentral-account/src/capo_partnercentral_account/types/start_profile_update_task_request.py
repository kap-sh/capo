"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#StartProfileUpdateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.partner_identifier
    import capo_partnercentral_account.types.task_details


class StartProfileUpdateTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>The unique identifier of the partner account.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    task_details: "capo_partnercentral_account.types.task_details.TaskDetails"
    """<p>The details of the profile updates to be performed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartProfileUpdateTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import capo_partnercentral_account.types.task_details

    out["TaskDetails"] = (
        capo_partnercentral_account.types.task_details.serialize_aws_json_1_0(
            value["task_details"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartProfileUpdateTaskRequest:
    out: StartProfileUpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("TaskDetails") is not None:
        import capo_partnercentral_account.types.task_details

        out["task_details"] = (
            capo_partnercentral_account.types.task_details.deserialize_aws_json_1_0(
                data["TaskDetails"]
            )
        )
    else:
        raise DeserializationError(
            "StartProfileUpdateTaskRequest.task_details required"
        )
    return out
