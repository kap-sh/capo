"""Generated from Smithy shape ``com.amazonaws.workspacesweb#TrustStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.arn_list


class TrustStore(TypedDict, closed=True):
    associated_portal_arns: NotRequired["capo_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this trust store is associated with.</p>"""
    trust_store_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustStore) -> dict:
    out: dict = {}
    if "associated_portal_arns" in value:
        import capo_workspaces_web.types.arn_list

        out["associatedPortalArns"] = capo_workspaces_web.types.arn_list.serialize_json(
            value["associated_portal_arns"]
        )
    out["trustStoreArn"] = value["trust_store_arn"]
    return out


def deserialize_json(data: dict) -> TrustStore:
    out: TrustStore = {}  # type: ignore[typeddict-item]
    if data.get("associatedPortalArns") is not None:
        import capo_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            capo_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if data.get("trustStoreArn") is not None:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        out["trust_store_arn"] = ""
    return out
