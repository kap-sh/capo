"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateNamespaceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.namespace


class UpdateNamespaceResponse(TypedDict, closed=True):
    namespace: "capo_redshift_serverless.types.namespace.Namespace"
    """<p>A list of tag instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNamespaceResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.namespace

    out["namespace"] = capo_redshift_serverless.types.namespace.serialize_aws_json_1_1(
        value["namespace"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNamespaceResponse:
    out: UpdateNamespaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = (
            capo_redshift_serverless.types.namespace.deserialize_aws_json_1_1(
                data["namespace"]
            )
        )
    else:
        raise DeserializationError("UpdateNamespaceResponse.namespace required")
    return out


def redact_sensitive(value: UpdateNamespaceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "namespace" in value:
        import capo_redshift_serverless.types.namespace

        out["namespace"] = capo_redshift_serverless.types.namespace.redact_sensitive(
            value["namespace"]
        )
    return out
