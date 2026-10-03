"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#DisassociateApplicationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.arn
    import capo_gameliftstreams.types.arn_list


class DisassociateApplicationsOutput(TypedDict, closed=True):
    arn: NotRequired["capo_gameliftstreams.types.arn.Arn"]
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. </p>"""
    application_arns: NotRequired["capo_gameliftstreams.types.arn_list.ArnList"]
    """<p>A set of applications that are disassociated from this stream group.</p> <p>This value is a set of <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Names (ARNs)</a> that uniquely identify application resources. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateApplicationsOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "application_arns" in value:
        import capo_gameliftstreams.types.arn_list

        out["ApplicationArns"] = capo_gameliftstreams.types.arn_list.serialize_json(
            value["application_arns"]
        )
    return out


def deserialize_json(data: dict) -> DisassociateApplicationsOutput:
    out: DisassociateApplicationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ApplicationArns") is not None:
        import capo_gameliftstreams.types.arn_list

        out["application_arns"] = capo_gameliftstreams.types.arn_list.deserialize_json(
            data["ApplicationArns"]
        )
    return out
