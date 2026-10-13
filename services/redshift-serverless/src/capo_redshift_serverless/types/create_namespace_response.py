"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#CreateNamespaceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace


class CreateNamespaceResponse(TypedDict, closed=True):
    namespace: NotRequired["capo_redshift_serverless.types.namespace.Namespace"]
    """<p>The created namespace object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNamespaceResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.serialize_aws_json_1_1(
                value["namespace"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNamespaceResponse:
    out: CreateNamespaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    return out


def redact_sensitive(value: CreateNamespaceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = capo_redshift_serverless.types.namespace.redact_sensitive(
            value["namespace"]
        )
    return out
