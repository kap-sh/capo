"""Generated from Smithy shape ``com.amazonaws.qapps#SubmissionMutation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.submission_mutation_kind
    import capo_qapps.types.uuid


class SubmissionMutation(TypedDict, closed=True):
    submission_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the submission.</p>"""
    mutation_type: "capo_qapps.types.submission_mutation_kind.SubmissionMutationKind"
    """<p>The operation that is performed on a submission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmissionMutation) -> dict:
    out: dict = {}
    out["submissionId"] = value["submission_id"]
    import capo_qapps.types.submission_mutation_kind

    out["mutationType"] = capo_qapps.types.submission_mutation_kind.serialize_json(
        value["mutation_type"]
    )
    return out


def deserialize_json(data: dict) -> SubmissionMutation:
    out: SubmissionMutation = {}  # type: ignore[typeddict-item]
    if data.get("submissionId") is not None:
        out["submission_id"] = data["submissionId"]
    else:
        out["submission_id"] = ""
    if data.get("mutationType") is not None:
        import capo_qapps.types.submission_mutation_kind

        out["mutation_type"] = (
            capo_qapps.types.submission_mutation_kind.deserialize_json(
                data["mutationType"]
            )
        )
    else:
        import typing

        out["mutation_type"] = typing.cast(
            "capo_qapps.types.submission_mutation_kind.SubmissionMutationKind", ""
        )
    return out
