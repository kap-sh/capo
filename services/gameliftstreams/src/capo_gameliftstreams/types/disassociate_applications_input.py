"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#DisassociateApplicationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.identifiers


class DisassociateApplicationsInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>A stream group to disassociate these applications from.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    application_identifiers: "capo_gameliftstreams.types.identifiers.Identifiers"
    """<p>A set of applications that you want to disassociate from the stream group.</p> <p>This value is a set of either <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Names (ARN)</a> or IDs that uniquely identify application resources. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateApplicationsInput) -> dict:
    out: dict = {}
    import capo_gameliftstreams.types.identifiers

    out["ApplicationIdentifiers"] = (
        capo_gameliftstreams.types.identifiers.serialize_json(
            value["application_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociateApplicationsInput:
    out: DisassociateApplicationsInput = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationIdentifiers") is not None:
        import capo_gameliftstreams.types.identifiers

        out["application_identifiers"] = (
            capo_gameliftstreams.types.identifiers.deserialize_json(
                data["ApplicationIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateApplicationsInput.application_identifiers required"
        )
    return out
