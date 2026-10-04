"""Generated from Smithy shape ``com.amazonaws.endusermessaging#UpdateBrandProfileFromRegistrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.job_results


class UpdateBrandProfileFromRegistrationOutput(TypedDict, closed=True):
    results: "capo_endusermessaging.types.job_results.JobResults"
    """<p>The results of the operation. Each result pairs a requested item with the asynchronous job that processes it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandProfileFromRegistrationOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.job_results

    out["results"] = capo_endusermessaging.types.job_results.serialize_json(
        value["results"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBrandProfileFromRegistrationOutput:
    out: UpdateBrandProfileFromRegistrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_endusermessaging.types.job_results

        out["results"] = capo_endusermessaging.types.job_results.deserialize_json(
            data["results"]
        )
    else:
        raise DeserializationError(
            "UpdateBrandProfileFromRegistrationOutput.results required"
        )
    return out
