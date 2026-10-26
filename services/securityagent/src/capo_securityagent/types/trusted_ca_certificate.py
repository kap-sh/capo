"""Generated from Smithy shape ``com.amazonaws.securityagent#TrustedCaCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.ca_certificate_source


class TrustedCaCertificate(TypedDict, closed=True):
    source: "capo_securityagent.types.ca_certificate_source.CaCertificateSource"
    """<p>The source that Security Agent reads the certificate from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrustedCaCertificate) -> dict:
    out: dict = {}
    import capo_securityagent.types.ca_certificate_source

    out["source"] = capo_securityagent.types.ca_certificate_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> TrustedCaCertificate:
    out: TrustedCaCertificate = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_securityagent.types.ca_certificate_source

        out["source"] = capo_securityagent.types.ca_certificate_source.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    return out
