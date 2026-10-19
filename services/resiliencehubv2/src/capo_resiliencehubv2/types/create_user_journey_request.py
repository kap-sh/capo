"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateUserJourneyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_label


class CreateUserJourneyRequest(TypedDict, closed=True):
    system_arn: "capo_resiliencehubv2.types.arn.Arn"
    name: "capo_resiliencehubv2.types.entity_label.EntityLabel"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserJourneyRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateUserJourneyRequest:
    out: CreateUserJourneyRequest = {}  # type: ignore[typeddict-item]
    if data.get("systemArn") is not None:
        out["system_arn"] = data["systemArn"]
    else:
        out["system_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
