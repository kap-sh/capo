"""Generated from Smithy shape ``com.amazonaws.eks#ListPodIdentityAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.pod_identity_association_summaries
    import capo_eks.types.string


class ListPodIdentityAssociationsResponse(TypedDict, closed=True):
    associations: NotRequired[
        "capo_eks.types.pod_identity_association_summaries.PodIdentityAssociationSummaries"
    ]
    """<p>The list of summarized descriptions of the associations that are in the cluster and match any filters that you provided.</p> <p>Each summary is simplified by removing these fields compared to the full <a href="https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociation.html"> <code>PodIdentityAssociation</code> </a>:</p> <ul> <li> <p>The IAM role: <code>roleArn</code> </p> </li> <li> <p>The timestamp that the association was created at: <code>createdAt</code> </p> </li> <li> <p>The most recent timestamp that the association was modified at:. <code>modifiedAt</code> </p> </li> <li> <p>The tags on the association: <code>tags</code> </p> </li> </ul>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListPodIdentityAssociations</code> request. When the results of a <code>ListPodIdentityAssociations</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPodIdentityAssociationsResponse) -> dict:
    out: dict = {}
    if "associations" in value:
        import capo_eks.types.pod_identity_association_summaries

        out["associations"] = (
            capo_eks.types.pod_identity_association_summaries.serialize_json(
                value["associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPodIdentityAssociationsResponse:
    out: ListPodIdentityAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("associations") is not None:
        import capo_eks.types.pod_identity_association_summaries

        out["associations"] = (
            capo_eks.types.pod_identity_association_summaries.deserialize_json(
                data["associations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
