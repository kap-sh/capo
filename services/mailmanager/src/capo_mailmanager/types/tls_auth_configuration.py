"""Generated from Smithy shape ``com.amazonaws.mailmanager#TlsAuthConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.trust_store


class TlsAuthConfiguration(TypedDict, closed=True):
    trust_store: NotRequired["capo_mailmanager.types.trust_store.TrustStore"]
    """<p>The trust store configuration for mutual TLS authentication.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TlsAuthConfiguration) -> dict:
    out: dict = {}
    if "trust_store" in value:
        import capo_mailmanager.types.trust_store

        out["TrustStore"] = capo_mailmanager.types.trust_store.serialize_aws_json_1_0(
            value["trust_store"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TlsAuthConfiguration:
    out: TlsAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TrustStore") is not None:
        import capo_mailmanager.types.trust_store

        out["trust_store"] = (
            capo_mailmanager.types.trust_store.deserialize_aws_json_1_0(
                data["TrustStore"]
            )
        )
    return out


def redact_sensitive(value: TlsAuthConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "trust_store" in value:
        import capo_mailmanager.types.trust_store

        out["trust_store"] = capo_mailmanager.types.trust_store.redact_sensitive(
            value["trust_store"]
        )
    return out
