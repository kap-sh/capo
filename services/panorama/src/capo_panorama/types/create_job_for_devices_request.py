"""Generated from Smithy shape ``com.amazonaws.panorama#CreateJobForDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_id_list
    import capo_panorama.types.device_job_config
    import capo_panorama.types.job_type


class CreateJobForDevicesRequest(TypedDict, closed=True):
    device_ids: "capo_panorama.types.device_id_list.DeviceIdList"
    """<p>ID of target device.</p>"""
    device_job_config: NotRequired[
        "capo_panorama.types.device_job_config.DeviceJobConfig"
    ]
    """<p>Configuration settings for a software update job.</p>"""
    job_type: "capo_panorama.types.job_type.JobType"
    """<p>The type of job to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobForDevicesRequest) -> dict:
    out: dict = {}
    import capo_panorama.types.device_id_list

    out["DeviceIds"] = capo_panorama.types.device_id_list.serialize_json(
        value["device_ids"]
    )
    if "device_job_config" in value:
        import capo_panorama.types.device_job_config

        out["DeviceJobConfig"] = capo_panorama.types.device_job_config.serialize_json(
            value["device_job_config"]
        )
    out["JobType"] = value["job_type"]
    return out


def deserialize_json(data: dict) -> CreateJobForDevicesRequest:
    out: CreateJobForDevicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceIds") is not None:
        import capo_panorama.types.device_id_list

        out["device_ids"] = capo_panorama.types.device_id_list.deserialize_json(
            data["DeviceIds"]
        )
    else:
        out["device_ids"] = []
    if data.get("DeviceJobConfig") is not None:
        import capo_panorama.types.device_job_config

        out["device_job_config"] = (
            capo_panorama.types.device_job_config.deserialize_json(
                data["DeviceJobConfig"]
            )
        )
    if data.get("JobType") is not None:
        out["job_type"] = data["JobType"]
    else:
        out["job_type"] = ""
    return out
