"""Generated from Smithy shape ``com.amazonaws.efs#PutLifecycleConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_efs.types.file_system_id
    import capo_efs.types.lifecycle_policies


class PutLifecycleConfigurationRequest(TypedDict, closed=True):
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system for which you are creating the <code>LifecycleConfiguration</code> object (String).</p>"""
    lifecycle_policies: "capo_efs.types.lifecycle_policies.LifecyclePolicies"
    """<p>An array of <code>LifecyclePolicy</code> objects that define the file system's <code>LifecycleConfiguration</code> object. A <code>LifecycleConfiguration</code> object informs lifecycle management of the following:</p> <ul> <li> <p> <b> <code>TransitionToIA</code> </b> – When to move files in the file system from primary storage (Standard storage class) into the Infrequent Access (IA) storage.</p> </li> <li> <p> <b> <code>TransitionToArchive</code> </b> – When to move files in the file system from their current storage class (either IA or Standard storage) into the Archive storage.</p> <p>File systems cannot transition into Archive storage before transitioning into IA storage. Therefore, TransitionToArchive must either not be set or must be later than TransitionToIA.</p> <note> <p>The Archive storage class is available only for file systems that use the Elastic throughput mode and the General Purpose performance mode. </p> </note> </li> <li> <p> <b> <code>TransitionToPrimaryStorageClass</code> </b> – Whether to move files in the file system back to primary storage (Standard storage class) after they are accessed in IA or Archive storage.</p> </li> </ul> <note> <p>When using the <code>put-lifecycle-configuration</code> CLI command or the <code>PutLifecycleConfiguration</code> API action, Amazon EFS requires that each <code>LifecyclePolicy</code> object have only a single transition. This means that in a request body, <code>LifecyclePolicies</code> must be structured as an array of <code>LifecyclePolicy</code> objects, one object for each storage transition. See the example requests in the following section for more information.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutLifecycleConfigurationRequest) -> dict:
    out: dict = {}
    import capo_efs.types.lifecycle_policies

    out["LifecyclePolicies"] = capo_efs.types.lifecycle_policies.serialize_json(
        value["lifecycle_policies"]
    )
    return out


def deserialize_json(data: dict) -> PutLifecycleConfigurationRequest:
    out: PutLifecycleConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("LifecyclePolicies") is not None:
        import capo_efs.types.lifecycle_policies

        out["lifecycle_policies"] = capo_efs.types.lifecycle_policies.deserialize_json(
            data["LifecyclePolicies"]
        )
    else:
        out["lifecycle_policies"] = []
    return out
