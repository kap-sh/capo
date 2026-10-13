"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteNamespaceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace


class DeleteNamespaceResponse(TypedDict, closed=True):
    namespace: "capo_redshift_serverless.types.namespace.Namespace"
    """<p>The deleted namespace object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamespaceResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.namespace

    out["namespace"] = capo_redshift_serverless.types.namespace.serialize_aws_json_1_1(
        value["namespace"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamespaceResponse:
    out: DeleteNamespaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    else:
        raise DeserializationError("DeleteNamespaceResponse.namespace required")
    return out


def redact_sensitive(value: DeleteNamespaceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = capo_redshift_serverless.types.namespace.redact_sensitive(
            value["namespace"]
        )
    return out
