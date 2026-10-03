"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateLinkModuleFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.module_configuration_list


class UpdateLinkModuleFlowRequest(TypedDict, closed=True):
    client_token: "str"
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>clientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    modules: "capo_rtbfabric.types.module_configuration_list.ModuleConfigurationList"
    """<p>The configuration of a module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLinkModuleFlowRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    import capo_rtbfabric.types.module_configuration_list

    out["modules"] = capo_rtbfabric.types.module_configuration_list.serialize_json(
        value["modules"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLinkModuleFlowRequest:
    out: UpdateLinkModuleFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateLinkModuleFlowRequest.client_token required")
    if data.get("modules") is not None:
        import capo_rtbfabric.types.module_configuration_list

        out["modules"] = (
            capo_rtbfabric.types.module_configuration_list.deserialize_json(
                data["modules"]
            )
        )
    else:
        raise DeserializationError("UpdateLinkModuleFlowRequest.modules required")
    return out
