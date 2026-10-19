"""Generated from Smithy shape ``com.amazonaws.fis#StartExperimentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.client_token
    import capo_fis.types.experiment_template_id
    import capo_fis.types.start_experiment_experiment_options_input
    import capo_fis.types.tag_map


class StartExperimentRequest(TypedDict, closed=True):
    client_token: "capo_fis.types.client_token.ClientToken"
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId"
    """<p>The ID of the experiment template.</p>"""
    experiment_options: NotRequired[
        "capo_fis.types.start_experiment_experiment_options_input.StartExperimentExperimentOptionsInput"
    ]
    """<p>The experiment options for running the experiment.</p>"""
    tags: NotRequired["capo_fis.types.tag_map.TagMap"]
    """<p>The tags to apply to the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExperimentRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["experimentTemplateId"] = value["experiment_template_id"]
    if "experiment_options" in value:
        import capo_fis.types.start_experiment_experiment_options_input

        out["experimentOptions"] = (
            capo_fis.types.start_experiment_experiment_options_input.serialize_json(
                value["experiment_options"]
            )
        )
    if "tags" in value:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartExperimentRequest:
    out: StartExperimentRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("experimentTemplateId") is not None:
        out["experiment_template_id"] = data["experimentTemplateId"]
    else:
        out["experiment_template_id"] = ""
    if data.get("experimentOptions") is not None:
        import capo_fis.types.start_experiment_experiment_options_input

        out["experiment_options"] = (
            capo_fis.types.start_experiment_experiment_options_input.deserialize_json(
                data["experimentOptions"]
            )
        )
    if data.get("tags") is not None:
        import capo_fis.types.tag_map

        out["tags"] = capo_fis.types.tag_map.deserialize_json(data["tags"])
    return out
