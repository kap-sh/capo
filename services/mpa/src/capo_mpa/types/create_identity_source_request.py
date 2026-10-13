"""Generated from Smithy shape ``com.amazonaws.mpa#CreateIdentitySourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mpa.types.identity_source_parameters
    import capo_mpa.types.tags
    import capo_mpa.types.token


class CreateIdentitySourceRequest(TypedDict, closed=True):
    identity_source_parameters: (
        "capo_mpa.types.identity_source_parameters.IdentitySourceParameters"
    )
    """<p>A <code> IdentitySourceParameters</code> object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.</p>"""
    client_token: NotRequired["capo_mpa.types.token.Token"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services populates this field.</p> <note> <p> <b>What is idempotency?</b> </p> <p>When you make a mutating API request, the request typically returns a result before the operation's asynchronous workflows have completed. Operations might also time out or encounter other server issues before they complete, even though the request has already returned a result. This could make it difficult to determine whether the request succeeded or not, and could lead to multiple retries to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation is completed multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p> </note>"""
    tags: NotRequired["capo_mpa.types.tags.Tags"]
    """<p>Tag you want to attach to the identity source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdentitySourceRequest) -> dict:
    out: dict = {}
    import capo_mpa.types.identity_source_parameters

    out["IdentitySourceParameters"] = (
        capo_mpa.types.identity_source_parameters.serialize_json(
            value["identity_source_parameters"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_mpa.types.tags

        out["Tags"] = capo_mpa.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIdentitySourceRequest:
    out: CreateIdentitySourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentitySourceParameters") is not None:
        import capo_mpa.types.identity_source_parameters

        out["identity_source_parameters"] = (
            capo_mpa.types.identity_source_parameters.deserialize_json(
                data["IdentitySourceParameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdentitySourceRequest.identity_source_parameters required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_mpa.types.tags

        out["tags"] = capo_mpa.types.tags.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: CreateIdentitySourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
