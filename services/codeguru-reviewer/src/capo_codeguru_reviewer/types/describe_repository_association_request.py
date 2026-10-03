"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#DescribeRepositoryAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.association_arn


class DescribeRepositoryAssociationRequest(TypedDict, closed=True):
    association_arn: "capo_codeguru_reviewer.types.association_arn.AssociationArn"
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRepositoryAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRepositoryAssociationRequest:
    out: DescribeRepositoryAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
