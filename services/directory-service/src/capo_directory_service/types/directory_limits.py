"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.cloud_only_directories_limit_reached
    import capo_directory_service.types.connected_directories_limit_reached
    import capo_directory_service.types.limit


class DirectoryLimits(TypedDict, closed=True):
    cloud_only_directories_limit: NotRequired[
        "capo_directory_service.types.limit.Limit"
    ]
    """<p>The maximum number of cloud directories allowed in the Region.</p>"""
    cloud_only_directories_current_count: NotRequired[
        "capo_directory_service.types.limit.Limit"
    ]
    """<p>The current number of cloud directories in the Region.</p>"""
    cloud_only_directories_limit_reached: "capo_directory_service.types.cloud_only_directories_limit_reached.CloudOnlyDirectoriesLimitReached"
    """<p>Indicates if the cloud directory limit has been reached.</p>"""
    cloud_only_microsoft_ad_limit: NotRequired[
        "capo_directory_service.types.limit.Limit"
    ]
    """<p>The maximum number of Managed Microsoft AD directories allowed in the region.</p>"""
    cloud_only_microsoft_ad_current_count: NotRequired[
        "capo_directory_service.types.limit.Limit"
    ]
    """<p>The current number of Managed Microsoft AD directories in the region.</p>"""
    cloud_only_microsoft_ad_limit_reached: "capo_directory_service.types.cloud_only_directories_limit_reached.CloudOnlyDirectoriesLimitReached"
    """<p>Indicates if the Managed Microsoft AD directory limit has been reached.</p>"""
    connected_directories_limit: NotRequired["capo_directory_service.types.limit.Limit"]
    """<p>The maximum number of connected directories allowed in the Region.</p>"""
    connected_directories_current_count: NotRequired[
        "capo_directory_service.types.limit.Limit"
    ]
    """<p>The current number of connected directories in the Region.</p>"""
    connected_directories_limit_reached: "capo_directory_service.types.connected_directories_limit_reached.ConnectedDirectoriesLimitReached"
    """<p>Indicates if the connected directory limit has been reached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryLimits) -> dict:
    out: dict = {}
    if "cloud_only_directories_limit" in value:
        out["CloudOnlyDirectoriesLimit"] = value["cloud_only_directories_limit"]
    if "cloud_only_directories_current_count" in value:
        out["CloudOnlyDirectoriesCurrentCount"] = value[
            "cloud_only_directories_current_count"
        ]
    out["CloudOnlyDirectoriesLimitReached"] = value.get(
        "cloud_only_directories_limit_reached", False
    )
    if "cloud_only_microsoft_ad_limit" in value:
        out["CloudOnlyMicrosoftADLimit"] = value["cloud_only_microsoft_ad_limit"]
    if "cloud_only_microsoft_ad_current_count" in value:
        out["CloudOnlyMicrosoftADCurrentCount"] = value[
            "cloud_only_microsoft_ad_current_count"
        ]
    out["CloudOnlyMicrosoftADLimitReached"] = value.get(
        "cloud_only_microsoft_ad_limit_reached", False
    )
    if "connected_directories_limit" in value:
        out["ConnectedDirectoriesLimit"] = value["connected_directories_limit"]
    if "connected_directories_current_count" in value:
        out["ConnectedDirectoriesCurrentCount"] = value[
            "connected_directories_current_count"
        ]
    out["ConnectedDirectoriesLimitReached"] = value.get(
        "connected_directories_limit_reached", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectoryLimits:
    out: DirectoryLimits = {}  # type: ignore[typeddict-item]
    if data.get("CloudOnlyDirectoriesLimit") is not None:
        out["cloud_only_directories_limit"] = data["CloudOnlyDirectoriesLimit"]
    if data.get("CloudOnlyDirectoriesCurrentCount") is not None:
        out["cloud_only_directories_current_count"] = data[
            "CloudOnlyDirectoriesCurrentCount"
        ]
    if data.get("CloudOnlyDirectoriesLimitReached") is not None:
        out["cloud_only_directories_limit_reached"] = data[
            "CloudOnlyDirectoriesLimitReached"
        ]
    else:
        out["cloud_only_directories_limit_reached"] = False
    if data.get("CloudOnlyMicrosoftADLimit") is not None:
        out["cloud_only_microsoft_ad_limit"] = data["CloudOnlyMicrosoftADLimit"]
    if data.get("CloudOnlyMicrosoftADCurrentCount") is not None:
        out["cloud_only_microsoft_ad_current_count"] = data[
            "CloudOnlyMicrosoftADCurrentCount"
        ]
    if data.get("CloudOnlyMicrosoftADLimitReached") is not None:
        out["cloud_only_microsoft_ad_limit_reached"] = data[
            "CloudOnlyMicrosoftADLimitReached"
        ]
    else:
        out["cloud_only_microsoft_ad_limit_reached"] = False
    if data.get("ConnectedDirectoriesLimit") is not None:
        out["connected_directories_limit"] = data["ConnectedDirectoriesLimit"]
    if data.get("ConnectedDirectoriesCurrentCount") is not None:
        out["connected_directories_current_count"] = data[
            "ConnectedDirectoriesCurrentCount"
        ]
    if data.get("ConnectedDirectoriesLimitReached") is not None:
        out["connected_directories_limit_reached"] = data[
            "ConnectedDirectoriesLimitReached"
        ]
    else:
        out["connected_directories_limit_reached"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DirectoryLimits) -> dict:
    out: dict = {}
    if "cloud_only_directories_limit" in value:
        out["CloudOnlyDirectoriesLimit"] = value["cloud_only_directories_limit"]
    if "cloud_only_directories_current_count" in value:
        out["CloudOnlyDirectoriesCurrentCount"] = value[
            "cloud_only_directories_current_count"
        ]
    out["CloudOnlyDirectoriesLimitReached"] = value.get(
        "cloud_only_directories_limit_reached", False
    )
    if "cloud_only_microsoft_ad_limit" in value:
        out["CloudOnlyMicrosoftADLimit"] = value["cloud_only_microsoft_ad_limit"]
    if "cloud_only_microsoft_ad_current_count" in value:
        out["CloudOnlyMicrosoftADCurrentCount"] = value[
            "cloud_only_microsoft_ad_current_count"
        ]
    out["CloudOnlyMicrosoftADLimitReached"] = value.get(
        "cloud_only_microsoft_ad_limit_reached", False
    )
    if "connected_directories_limit" in value:
        out["ConnectedDirectoriesLimit"] = value["connected_directories_limit"]
    if "connected_directories_current_count" in value:
        out["ConnectedDirectoriesCurrentCount"] = value[
            "connected_directories_current_count"
        ]
    out["ConnectedDirectoriesLimitReached"] = value.get(
        "connected_directories_limit_reached", False
    )
    return out


def deserialize_cbor(data: dict) -> DirectoryLimits:
    out: DirectoryLimits = {}  # type: ignore[typeddict-item]
    if data.get("CloudOnlyDirectoriesLimit") is not None:
        out["cloud_only_directories_limit"] = data["CloudOnlyDirectoriesLimit"]
    if data.get("CloudOnlyDirectoriesCurrentCount") is not None:
        out["cloud_only_directories_current_count"] = data[
            "CloudOnlyDirectoriesCurrentCount"
        ]
    if data.get("CloudOnlyDirectoriesLimitReached") is not None:
        out["cloud_only_directories_limit_reached"] = data[
            "CloudOnlyDirectoriesLimitReached"
        ]
    else:
        out["cloud_only_directories_limit_reached"] = False
    if data.get("CloudOnlyMicrosoftADLimit") is not None:
        out["cloud_only_microsoft_ad_limit"] = data["CloudOnlyMicrosoftADLimit"]
    if data.get("CloudOnlyMicrosoftADCurrentCount") is not None:
        out["cloud_only_microsoft_ad_current_count"] = data[
            "CloudOnlyMicrosoftADCurrentCount"
        ]
    if data.get("CloudOnlyMicrosoftADLimitReached") is not None:
        out["cloud_only_microsoft_ad_limit_reached"] = data[
            "CloudOnlyMicrosoftADLimitReached"
        ]
    else:
        out["cloud_only_microsoft_ad_limit_reached"] = False
    if data.get("ConnectedDirectoriesLimit") is not None:
        out["connected_directories_limit"] = data["ConnectedDirectoriesLimit"]
    if data.get("ConnectedDirectoriesCurrentCount") is not None:
        out["connected_directories_current_count"] = data[
            "ConnectedDirectoriesCurrentCount"
        ]
    if data.get("ConnectedDirectoriesLimitReached") is not None:
        out["connected_directories_limit_reached"] = data[
            "ConnectedDirectoriesLimitReached"
        ]
    else:
        out["connected_directories_limit_reached"] = False
    return out
