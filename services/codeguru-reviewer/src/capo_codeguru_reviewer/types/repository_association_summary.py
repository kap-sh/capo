"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.arn
    import capo_codeguru_reviewer.types.association_id
    import capo_codeguru_reviewer.types.connection_arn
    import capo_codeguru_reviewer.types.name
    import capo_codeguru_reviewer.types.owner
    import capo_codeguru_reviewer.types.provider_type
    import capo_codeguru_reviewer.types.repository_association_state
    import capo_codeguru_reviewer.types.time_stamp


class RepositoryAssociationSummary(TypedDict, closed=True):
    association_arn: NotRequired["capo_codeguru_reviewer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html">RepositoryAssociation</a> object. You can retrieve this ARN by calling <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html">ListRepositoryAssociations</a>.</p>"""
    connection_arn: NotRequired[
        "capo_codeguru_reviewer.types.connection_arn.ConnectionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services CodeStar Connections connection. Its format is <code>arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id</code>. For more information, see <a href="https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html">Connection</a> in the <i>Amazon Web Services CodeStar Connections API Reference</i>.</p>"""
    last_updated_time_stamp: NotRequired[
        "capo_codeguru_reviewer.types.time_stamp.TimeStamp"
    ]
    """<p>The time, in milliseconds since the epoch, since the repository association was last updated.</p>"""
    association_id: NotRequired[
        "capo_codeguru_reviewer.types.association_id.AssociationId"
    ]
    """<p>The repository association ID.</p>"""
    name: NotRequired["capo_codeguru_reviewer.types.name.Name"]
    """<p>The name of the repository association.</p>"""
    owner: NotRequired["capo_codeguru_reviewer.types.owner.Owner"]
    """<p>The owner of the repository. For an Amazon Web Services CodeCommit repository, this is the Amazon Web Services account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or Amazon Web Services account ID.</p>"""
    provider_type: NotRequired[
        "capo_codeguru_reviewer.types.provider_type.ProviderType"
    ]
    """<p>The provider type of the repository association.</p>"""
    state: NotRequired[
        "capo_codeguru_reviewer.types.repository_association_state.RepositoryAssociationState"
    ]
    """<p>The state of the repository association.</p> <p>The valid repository association states are:</p> <ul> <li> <p> <b>Associated</b>: The repository association is complete.</p> </li> <li> <p> <b>Associating</b>: CodeGuru Reviewer is:</p> <ul> <li> <p>Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.</p> <note> <p>If your repository <code>ProviderType</code> is <code>GitHub</code>, <code>GitHub Enterprise Server</code>, or <code>Bitbucket</code>, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.</p> </note> </li> <li> <p>Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.</p> </li> </ul> </li> <li> <p> <b>Failed</b>: The repository failed to associate or disassociate.</p> </li> <li> <p> <b>Disassociating</b>: CodeGuru Reviewer is removing the repository's pull request notifications and source code access.</p> </li> <li> <p> <b>Disassociated</b>: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html">Using tags to control access to associated repositories</a> in the <i>Amazon CodeGuru Reviewer User Guide</i>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryAssociationSummary) -> dict:
    out: dict = {}
    if "association_arn" in value:
        out["AssociationArn"] = value["association_arn"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "last_updated_time_stamp" in value:
        import capo_codeguru_reviewer.types.time_stamp

        out["LastUpdatedTimeStamp"] = (
            capo_codeguru_reviewer.types.time_stamp.serialize_json(
                value["last_updated_time_stamp"]
            )
        )
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "provider_type" in value:
        import capo_codeguru_reviewer.types.provider_type

        out["ProviderType"] = capo_codeguru_reviewer.types.provider_type.serialize_json(
            value["provider_type"]
        )
    if "state" in value:
        import capo_codeguru_reviewer.types.repository_association_state

        out["State"] = (
            capo_codeguru_reviewer.types.repository_association_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> RepositoryAssociationSummary:
    out: RepositoryAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("AssociationArn") is not None:
        out["association_arn"] = data["AssociationArn"]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    if data.get("LastUpdatedTimeStamp") is not None:
        import capo_codeguru_reviewer.types.time_stamp

        out["last_updated_time_stamp"] = (
            capo_codeguru_reviewer.types.time_stamp.deserialize_json(
                data["LastUpdatedTimeStamp"]
            )
        )
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("ProviderType") is not None:
        import capo_codeguru_reviewer.types.provider_type

        out["provider_type"] = (
            capo_codeguru_reviewer.types.provider_type.deserialize_json(
                data["ProviderType"]
            )
        )
    if data.get("State") is not None:
        import capo_codeguru_reviewer.types.repository_association_state

        out["state"] = (
            capo_codeguru_reviewer.types.repository_association_state.deserialize_json(
                data["State"]
            )
        )
    return out
