"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ThirdPartySourceRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.connection_arn
    import capo_codeguru_reviewer.types.name
    import capo_codeguru_reviewer.types.owner


class ThirdPartySourceRepository(TypedDict, closed=True):
    name: "capo_codeguru_reviewer.types.name.Name"
    """<p>The name of the third party source repository.</p>"""
    connection_arn: "capo_codeguru_reviewer.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services CodeStar Connections connection. Its format is <code>arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id</code>. For more information, see <a href="https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html">Connection</a> in the <i>Amazon Web Services CodeStar Connections API Reference</i>.</p>"""
    owner: "capo_codeguru_reviewer.types.owner.Owner"
    """<p>The owner of the repository. For a GitHub, GitHub Enterprise, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, this can be the username or Amazon Web Services account ID </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThirdPartySourceRepository) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConnectionArn"] = value["connection_arn"]
    out["Owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> ThirdPartySourceRepository:
    out: ThirdPartySourceRepository = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ThirdPartySourceRepository.name required")
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError("ThirdPartySourceRepository.connection_arn required")
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    else:
        raise DeserializationError("ThirdPartySourceRepository.owner required")
    return out
