"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DeleteAppInputSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_input_source
    import capo_resiliencehub.types.arn


class DeleteAppInputSourceResponse(TypedDict, closed=True):
    app_arn: NotRequired["capo_resiliencehub.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_input_source: NotRequired[
        "capo_resiliencehub.types.app_input_source.AppInputSource"
    ]
    """<p>Name of the input source from where the application resource is imported from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAppInputSourceResponse) -> dict:
    out: dict = {}
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "app_input_source" in value:
        import capo_resiliencehub.types.app_input_source

        out["appInputSource"] = (
            capo_resiliencehub.types.app_input_source.serialize_json(
                value["app_input_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteAppInputSourceResponse:
    out: DeleteAppInputSourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("appInputSource") is not None:
        import capo_resiliencehub.types.app_input_source

        out["app_input_source"] = (
            capo_resiliencehub.types.app_input_source.deserialize_json(
                data["appInputSource"]
            )
        )
    return out
