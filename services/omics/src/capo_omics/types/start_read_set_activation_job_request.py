"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetActivationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.client_token
    import capo_omics.types.sequence_store_id
    import capo_omics.types.start_read_set_activation_job_source_list


class StartReadSetActivationJobRequest(TypedDict, closed=True):
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    client_token: NotRequired["capo_omics.types.client_token.ClientToken"]
    """<p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>"""
    sources: "capo_omics.types.start_read_set_activation_job_source_list.StartReadSetActivationJobSourceList"
    """<p>The job's source files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetActivationJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_omics.types.start_read_set_activation_job_source_list

    out["sources"] = (
        capo_omics.types.start_read_set_activation_job_source_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartReadSetActivationJobRequest:
    out: StartReadSetActivationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("sources") is not None:
        import capo_omics.types.start_read_set_activation_job_source_list

        out["sources"] = (
            capo_omics.types.start_read_set_activation_job_source_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    return out
