"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.certificate_location


class Certificate(TypedDict, closed=True):
    location: "capo_bedrock_agentcore.types.certificate_location.CertificateLocation"
    """<p>The location of the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Certificate) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.certificate_location

    out["location"] = capo_bedrock_agentcore.types.certificate_location.serialize_json(
        value["location"]
    )
    return out


def deserialize_json(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        import capo_bedrock_agentcore.types.certificate_location

        out["location"] = (
            capo_bedrock_agentcore.types.certificate_location.deserialize_json(
                data["location"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["location"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
    return out
