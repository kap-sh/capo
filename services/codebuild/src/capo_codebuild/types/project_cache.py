"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectCache``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.cache_type
    import capo_codebuild.types.project_cache_modes
    import capo_codebuild.types.string


class ProjectCache(TypedDict, closed=True):
    type: "capo_codebuild.types.cache_type.CacheType"
    """<p>The type of cache used by the build project. Valid values include:</p> <ul> <li> <p> <code>NO_CACHE</code>: The build project does not use any cache.</p> </li> <li> <p> <code>S3</code>: The build project reads and writes from and to S3.</p> </li> <li> <p> <code>LOCAL</code>: The build project stores a cache locally on a build host that is only available to that build host.</p> </li> </ul>"""
    location: NotRequired["capo_codebuild.types.string.String"]
    """<p>Information about the cache location: </p> <ul> <li> <p> <code>NO_CACHE</code> or <code>LOCAL</code>: This value is ignored.</p> </li> <li> <p> <code>S3</code>: This is the S3 bucket name/prefix.</p> </li> </ul>"""
    modes: NotRequired["capo_codebuild.types.project_cache_modes.ProjectCacheModes"]
    """<p>An array of strings that specify the local cache modes. You can use one or more local cache modes at the same time. This is only used for <code>LOCAL</code> cache types.</p> <p>Possible values are:</p> <dl> <dt>LOCAL_SOURCE_CACHE</dt> <dd> <p>Caches Git metadata for primary and secondary sources. After the cache is created, subsequent builds pull only the change between commits. This mode is a good choice for projects with a clean working directory and a source that is a large Git repository. If you choose this option and your project does not use a Git repository (GitHub, GitHub Enterprise, or Bitbucket), the option is ignored. </p> </dd> <dt>LOCAL_DOCKER_LAYER_CACHE</dt> <dd> <p>Caches existing Docker layers. This mode is a good choice for projects that build or pull large Docker images. It can prevent the performance issues caused by pulling large Docker images down from the network. </p> <note> <ul> <li> <p>You can use a Docker layer cache in the Linux environment only. </p> </li> <li> <p>The <code>privileged</code> flag must be set so that your project has the required Docker permissions. </p> </li> <li> <p>You should consider the security implications before you use a Docker layer cache. </p> </li> </ul> </note> </dd> <dt>LOCAL_CUSTOM_CACHE</dt> <dd> <p>Caches directories you specify in the buildspec file. This mode is a good choice if your build scenario is not suited to one of the other three local cache modes. If you use a custom cache: </p> <ul> <li> <p>Only directories can be specified for caching. You cannot specify individual files. </p> </li> <li> <p>Symlinks are used to reference cached directories. </p> </li> <li> <p>Cached directories are linked to your build before it downloads its project sources. Cached items are overridden if a source item has the same name. Directories are specified using cache paths in the buildspec file. </p> </li> </ul> </dd> </dl>"""
    cache_namespace: NotRequired["capo_codebuild.types.string.String"]
    """<p>Defines the scope of the cache. You can use this namespace to share a cache across multiple projects. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/caching-s3.html#caching-s3-sharing">Cache sharing between projects</a> in the <i>CodeBuild User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectCache) -> dict:
    out: dict = {}
    import capo_codebuild.types.cache_type

    out["type"] = capo_codebuild.types.cache_type.serialize_aws_json_1_1(value["type"])
    if "location" in value:
        out["location"] = value["location"]
    if "modes" in value:
        import capo_codebuild.types.project_cache_modes

        out["modes"] = capo_codebuild.types.project_cache_modes.serialize_aws_json_1_1(
            value["modes"]
        )
    if "cache_namespace" in value:
        out["cacheNamespace"] = value["cache_namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectCache:
    out: ProjectCache = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.cache_type

        out["type"] = capo_codebuild.types.cache_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("ProjectCache.type required")
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("modes") is not None:
        import capo_codebuild.types.project_cache_modes

        out["modes"] = (
            capo_codebuild.types.project_cache_modes.deserialize_aws_json_1_1(
                data["modes"]
            )
        )
    if data.get("cacheNamespace") is not None:
        out["cache_namespace"] = data["cacheNamespace"]
    return out
