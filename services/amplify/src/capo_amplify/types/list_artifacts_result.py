"""Generated from Smithy shape ``com.amazonaws.amplify#ListArtifactsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.artifacts
    import capo_amplify.types.next_token


class ListArtifactsResult(TypedDict, closed=True):
    artifacts: "capo_amplify.types.artifacts.Artifacts"
    """<p>A list of artifacts. </p>"""
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListArtifactsResult) -> dict:
    out: dict = {}
    import capo_amplify.types.artifacts

    out["artifacts"] = capo_amplify.types.artifacts.serialize_json(value["artifacts"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListArtifactsResult:
    out: ListArtifactsResult = {}  # type: ignore[typeddict-item]
    if data.get("artifacts") is not None:
        import capo_amplify.types.artifacts

        out["artifacts"] = capo_amplify.types.artifacts.deserialize_json(
            data["artifacts"]
        )
    else:
        out["artifacts"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
