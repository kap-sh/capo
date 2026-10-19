"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateInputSourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.resource_configuration


class CreateInputSourceRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    resource_configuration: (
        "capo_resiliencehubv2.types.resource_configuration.ResourceConfiguration"
    )
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateInputSourceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    import capo_resiliencehubv2.types.resource_configuration

    out["resourceConfiguration"] = (
        capo_resiliencehubv2.types.resource_configuration.serialize_json(
            value["resource_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateInputSourceRequest:
    out: CreateInputSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("resourceConfiguration") is not None:
        import capo_resiliencehubv2.types.resource_configuration

        out["resource_configuration"] = (
            capo_resiliencehubv2.types.resource_configuration.deserialize_json(
                data["resourceConfiguration"]
            )
        )
    else:
        import capo_resiliencehubv2.types._unknown

        out["resource_configuration"] = (
            capo_resiliencehubv2.types._unknown.UnknownUnionMember("")
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateInputSourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resource_configuration" in value:
        import capo_resiliencehubv2.types.resource_configuration

        out["resource_configuration"] = (
            capo_resiliencehubv2.types.resource_configuration.redact_sensitive(
                value["resource_configuration"]
            )
        )
    return out
