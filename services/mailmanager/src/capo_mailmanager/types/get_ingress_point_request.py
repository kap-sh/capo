"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetIngressPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.trust_store_response_option


class GetIngressPointRequest(TypedDict, closed=True):
    ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId"
    """<p>The identifier of an ingress endpoint.</p>"""
    include_trust_store_contents: NotRequired[
        "capo_mailmanager.types.trust_store_response_option.TrustStoreResponseOption"
    ]
    """<p>Whether to include the trust store contents in the response. Use INCLUDE to retrieve trust store certificate and CRL contents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIngressPointRequest) -> dict:
    out: dict = {}
    out["IngressPointId"] = value["ingress_point_id"]
    if "include_trust_store_contents" in value:
        import capo_mailmanager.types.trust_store_response_option

        out["IncludeTrustStoreContents"] = (
            capo_mailmanager.types.trust_store_response_option.serialize_aws_json_1_0(
                value["include_trust_store_contents"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIngressPointRequest:
    out: GetIngressPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("IngressPointId") is not None:
        out["ingress_point_id"] = data["IngressPointId"]
    else:
        out["ingress_point_id"] = ""
    if data.get("IncludeTrustStoreContents") is not None:
        import capo_mailmanager.types.trust_store_response_option

        out["include_trust_store_contents"] = (
            capo_mailmanager.types.trust_store_response_option.deserialize_aws_json_1_0(
                data["IncludeTrustStoreContents"]
            )
        )
    return out
