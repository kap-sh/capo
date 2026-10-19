"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.create_job_output
    import capo_elastic_transcoder.types.create_job_outputs
    import capo_elastic_transcoder.types.create_job_playlists
    import capo_elastic_transcoder.types.id
    import capo_elastic_transcoder.types.job_input
    import capo_elastic_transcoder.types.job_inputs
    import capo_elastic_transcoder.types.key
    import capo_elastic_transcoder.types.user_metadata


class CreateJobRequest(TypedDict, closed=True):
    pipeline_id: "capo_elastic_transcoder.types.id.Id"
    """<p>The <code>Id</code> of the pipeline that you want Elastic Transcoder to use for transcoding. The pipeline determines several settings, including the Amazon S3 bucket from which Elastic Transcoder gets the files to transcode and the bucket into which Elastic Transcoder puts the transcoded files.</p>"""
    input: NotRequired["capo_elastic_transcoder.types.job_input.JobInput"]
    """<p>A section of the request body that provides information about the file that is being transcoded.</p>"""
    inputs: NotRequired["capo_elastic_transcoder.types.job_inputs.JobInputs"]
    """<p>A section of the request body that provides information about the files that are being transcoded.</p>"""
    output: NotRequired[
        "capo_elastic_transcoder.types.create_job_output.CreateJobOutput"
    ]
    """<p> A section of the request body that provides information about the transcoded (target) file. We strongly recommend that you use the <code>Outputs</code> syntax instead of the <code>Output</code> syntax. </p>"""
    outputs: NotRequired[
        "capo_elastic_transcoder.types.create_job_outputs.CreateJobOutputs"
    ]
    """<p> A section of the request body that provides information about the transcoded (target) files. We recommend that you use the <code>Outputs</code> syntax instead of the <code>Output</code> syntax. </p>"""
    output_key_prefix: NotRequired["capo_elastic_transcoder.types.key.Key"]
    """<p>The value, if any, that you want Elastic Transcoder to prepend to the names of all files that this job creates, including output files, thumbnails, and playlists.</p>"""
    playlists: NotRequired[
        "capo_elastic_transcoder.types.create_job_playlists.CreateJobPlaylists"
    ]
    """<p>If you specify a preset in <code>PresetId</code> for which the value of <code>Container</code> is fmp4 (Fragmented MP4) or ts (MPEG-TS), Playlists contains information about the master playlists that you want Elastic Transcoder to create.</p> <p>The maximum number of master playlists in a job is 30.</p>"""
    user_metadata: NotRequired[
        "capo_elastic_transcoder.types.user_metadata.UserMetadata"
    ]
    """<p>User-defined metadata that you want to associate with an Elastic Transcoder job. You specify metadata in <code>key/value</code> pairs, and you can add up to 10 <code>key/value</code> pairs per job. Elastic Transcoder does not guarantee that <code>key/value</code> pairs are returned in the same order in which you specify them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    out["PipelineId"] = value["pipeline_id"]
    if "input" in value:
        import capo_elastic_transcoder.types.job_input

        out["Input"] = capo_elastic_transcoder.types.job_input.serialize_json(
            value["input"]
        )
    if "inputs" in value:
        import capo_elastic_transcoder.types.job_inputs

        out["Inputs"] = capo_elastic_transcoder.types.job_inputs.serialize_json(
            value["inputs"]
        )
    if "output" in value:
        import capo_elastic_transcoder.types.create_job_output

        out["Output"] = capo_elastic_transcoder.types.create_job_output.serialize_json(
            value["output"]
        )
    if "outputs" in value:
        import capo_elastic_transcoder.types.create_job_outputs

        out["Outputs"] = (
            capo_elastic_transcoder.types.create_job_outputs.serialize_json(
                value["outputs"]
            )
        )
    if "output_key_prefix" in value:
        out["OutputKeyPrefix"] = value["output_key_prefix"]
    if "playlists" in value:
        import capo_elastic_transcoder.types.create_job_playlists

        out["Playlists"] = (
            capo_elastic_transcoder.types.create_job_playlists.serialize_json(
                value["playlists"]
            )
        )
    if "user_metadata" in value:
        import capo_elastic_transcoder.types.user_metadata

        out["UserMetadata"] = (
            capo_elastic_transcoder.types.user_metadata.serialize_json(
                value["user_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineId") is not None:
        out["pipeline_id"] = data["PipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("Input") is not None:
        import capo_elastic_transcoder.types.job_input

        out["input"] = capo_elastic_transcoder.types.job_input.deserialize_json(
            data["Input"]
        )
    if data.get("Inputs") is not None:
        import capo_elastic_transcoder.types.job_inputs

        out["inputs"] = capo_elastic_transcoder.types.job_inputs.deserialize_json(
            data["Inputs"]
        )
    if data.get("Output") is not None:
        import capo_elastic_transcoder.types.create_job_output

        out["output"] = (
            capo_elastic_transcoder.types.create_job_output.deserialize_json(
                data["Output"]
            )
        )
    if data.get("Outputs") is not None:
        import capo_elastic_transcoder.types.create_job_outputs

        out["outputs"] = (
            capo_elastic_transcoder.types.create_job_outputs.deserialize_json(
                data["Outputs"]
            )
        )
    if data.get("OutputKeyPrefix") is not None:
        out["output_key_prefix"] = data["OutputKeyPrefix"]
    if data.get("Playlists") is not None:
        import capo_elastic_transcoder.types.create_job_playlists

        out["playlists"] = (
            capo_elastic_transcoder.types.create_job_playlists.deserialize_json(
                data["Playlists"]
            )
        )
    if data.get("UserMetadata") is not None:
        import capo_elastic_transcoder.types.user_metadata

        out["user_metadata"] = (
            capo_elastic_transcoder.types.user_metadata.deserialize_json(
                data["UserMetadata"]
            )
        )
    return out
