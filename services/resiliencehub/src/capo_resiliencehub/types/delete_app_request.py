"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.client_token


class DeleteAppRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    force_delete: NotRequired[
        "capo_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>A boolean option to force the deletion of an Resilience Hub application. </p>"""
    client_token: NotRequired["capo_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "force_delete" in value:
        out["forceDelete"] = value["force_delete"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteAppRequest:
    out: DeleteAppRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("DeleteAppRequest.app_arn required")
    if data.get("forceDelete") is not None:
        out["force_delete"] = data["forceDelete"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
