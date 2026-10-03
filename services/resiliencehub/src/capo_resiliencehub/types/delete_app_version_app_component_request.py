"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppVersionAppComponentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.client_token
    import capo_resiliencehub.types.string255


class DeleteAppVersionAppComponentRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    id: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the Application Component.</p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppVersionAppComponentRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["id"] = value["id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteAppVersionAppComponentRequest:
    out: DeleteAppVersionAppComponentRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DeleteAppVersionAppComponentRequest.app_arn required"
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteAppVersionAppComponentRequest.id required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
