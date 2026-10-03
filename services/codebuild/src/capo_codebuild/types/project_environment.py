"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.compute_configuration
    import capo_codebuild.types.compute_type
    import capo_codebuild.types.docker_server
    import capo_codebuild.types.environment_type
    import capo_codebuild.types.environment_variables
    import capo_codebuild.types.host_kernel
    import capo_codebuild.types.image_pull_credentials_type
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_fleet
    import capo_codebuild.types.registry_credential
    import capo_codebuild.types.string
    import capo_codebuild.types.wrapper_boolean


class ProjectEnvironment(TypedDict, closed=True):
    type: "capo_codebuild.types.environment_type.EnvironmentType"
    """<p>The type of build environment to use for related builds.</p> <note> <p>If you're using compute fleets during project creation, <code>type</code> will be ignored.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html">Build environment compute types</a> in the <i>CodeBuild user guide</i>.</p>"""
    image: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The image tag or image digest that identifies the Docker image to use for this build project. Use the following formats:</p> <ul> <li> <p>For an image tag: <code><registry>/<repository>:<tag></code>. For example, in the Docker repository that CodeBuild uses to manage its Docker images, this would be <code>aws/codebuild/standard:4.0</code>. </p> </li> <li> <p>For an image digest: <code><registry>/<repository>@<digest></code>. For example, to specify an image with the digest "sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf," use <code><registry>/<repository>@sha256:cbbf2f9a99b47fc460d422812b6a5adff7dfee951d8fa2e4a98caa0382cfbdbf</code>.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html">Docker images provided by CodeBuild</a> in the <i>CodeBuild user guide</i>.</p>"""
    compute_type: "capo_codebuild.types.compute_type.ComputeType"
    """<p>Information about the compute resources the build project uses. Available values include:</p> <ul> <li> <p> <code>ATTRIBUTE_BASED_COMPUTE</code>: Specify the amount of vCPUs, memory, disk space, and the type of machine.</p> <note> <p> If you use <code>ATTRIBUTE_BASED_COMPUTE</code>, you must define your attributes by using <code>computeConfiguration</code>. CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types">Reserved capacity environment types</a> in the <i>CodeBuild User Guide</i>.</p> </note> </li> <li> <p> <code>BUILD_GENERAL1_SMALL</code>: Use up to 4 GiB memory and 2 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_MEDIUM</code>: Use up to 8 GiB memory and 4 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_LARGE</code>: Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_XLARGE</code>: Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_2XLARGE</code>: Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.</p> </li> <li> <p> <code>BUILD_LAMBDA_1GB</code>: Use up to 1 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_2GB</code>: Use up to 2 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_4GB</code>: Use up to 4 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_8GB</code>: Use up to 8 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_10GB</code>: Use up to 10 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_SMALL</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_LARGE</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types">On-demand environment types</a> in the <i>CodeBuild User Guide.</i> </p>"""
    compute_configuration: NotRequired[
        "capo_codebuild.types.compute_configuration.ComputeConfiguration"
    ]
    """<p>The compute configuration of the build project. This is only required if <code>computeType</code> is set to <code>ATTRIBUTE_BASED_COMPUTE</code>.</p>"""
    fleet: NotRequired["capo_codebuild.types.project_fleet.ProjectFleet"]
    """<p>A ProjectFleet object to use for this build project.</p>"""
    environment_variables: NotRequired[
        "capo_codebuild.types.environment_variables.EnvironmentVariables"
    ]
    """<p>A set of environment variables to make available to builds for this build project.</p>"""
    privileged_mode: NotRequired["capo_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p>Enables running the Docker daemon inside a Docker container. Set to true only if the build project is used to build Docker images. Otherwise, a build that attempts to interact with the Docker daemon fails. The default setting is <code>false</code>.</p> <p>You can initialize the Docker daemon during the install phase of your build by adding one of the following sets of commands to the install phase of your buildspec file:</p> <p>If the operating system's base image is Ubuntu Linux:</p> <p> <code>- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&</code> </p> <p> <code>- timeout 15 sh -c "until docker info; do echo .; sleep 1; done"</code> </p> <p>If the operating system's base image is Alpine Linux and the previous command does not work, add the <code>-t</code> argument to <code>timeout</code>:</p> <p> <code>- nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://0.0.0.0:2375 --storage-driver=overlay&</code> </p> <p> <code>- timeout -t 15 sh -c "until docker info; do echo .; sleep 1; done"</code> </p>"""
    certificate: NotRequired["capo_codebuild.types.string.String"]
    """<p>The ARN of the Amazon S3 bucket, path prefix, and object key that contains the PEM-encoded certificate for the build project. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/create-project-cli.html#cli.environment.certificate">certificate</a> in the <i>CodeBuild User Guide</i>.</p>"""
    registry_credential: NotRequired[
        "capo_codebuild.types.registry_credential.RegistryCredential"
    ]
    """<p> The credentials for access to a private registry.</p>"""
    image_pull_credentials_type: NotRequired[
        "capo_codebuild.types.image_pull_credentials_type.ImagePullCredentialsType"
    ]
    """<p> The type of credentials CodeBuild uses to pull images in your build. There are two valid values: </p> <ul> <li> <p> <code>CODEBUILD</code> specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust CodeBuild service principal. </p> </li> <li> <p> <code>SERVICE_ROLE</code> specifies that CodeBuild uses your build project's service role. </p> </li> </ul> <p> When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an CodeBuild curated image, you must use CODEBUILD credentials. </p>"""
    docker_server: NotRequired["capo_codebuild.types.docker_server.DockerServer"]
    """<p>A DockerServer object to use for this build project.</p>"""
    host_kernel: NotRequired["capo_codebuild.types.host_kernel.HostKernel"]
    """<p>The host operating system kernel used for on-demand builds in the build project. The host kernel does not affect the build environment operating system, which is determined by the image you specify. Valid values are:</p> <ul> <li> <p> <code>LINUX_KERNEL_4</code>: Runs on an Amazon Linux 2 host (kernel 4.x).</p> </li> <li> <p> <code>LINUX_KERNEL_6</code>: Runs on an Amazon Linux 2023 host (kernel 6.x).</p> </li> <li> <p> <code>LINUX_KERNEL_LATEST</code>: Runs on the latest supported host kernel.</p> </li> </ul> <p>This setting applies to the <code>LINUX_CONTAINER</code>, <code>ARM_CONTAINER</code>, <code>LINUX_EC2</code>, and <code>ARM_EC2</code> environment types. It is not applicable to Windows, Lambda, or Mac environment types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectEnvironment) -> dict:
    out: dict = {}
    import capo_codebuild.types.environment_type

    out["type"] = capo_codebuild.types.environment_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["image"] = value["image"]
    import capo_codebuild.types.compute_type

    out["computeType"] = capo_codebuild.types.compute_type.serialize_aws_json_1_1(
        value["compute_type"]
    )
    if "compute_configuration" in value:
        import capo_codebuild.types.compute_configuration

        out["computeConfiguration"] = (
            capo_codebuild.types.compute_configuration.serialize_aws_json_1_1(
                value["compute_configuration"]
            )
        )
    if "fleet" in value:
        import capo_codebuild.types.project_fleet

        out["fleet"] = capo_codebuild.types.project_fleet.serialize_aws_json_1_1(
            value["fleet"]
        )
    if "environment_variables" in value:
        import capo_codebuild.types.environment_variables

        out["environmentVariables"] = (
            capo_codebuild.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    if "privileged_mode" in value:
        out["privilegedMode"] = value["privileged_mode"]
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    if "registry_credential" in value:
        import capo_codebuild.types.registry_credential

        out["registryCredential"] = (
            capo_codebuild.types.registry_credential.serialize_aws_json_1_1(
                value["registry_credential"]
            )
        )
    if "image_pull_credentials_type" in value:
        import capo_codebuild.types.image_pull_credentials_type

        out["imagePullCredentialsType"] = (
            capo_codebuild.types.image_pull_credentials_type.serialize_aws_json_1_1(
                value["image_pull_credentials_type"]
            )
        )
    if "docker_server" in value:
        import capo_codebuild.types.docker_server

        out["dockerServer"] = capo_codebuild.types.docker_server.serialize_aws_json_1_1(
            value["docker_server"]
        )
    if "host_kernel" in value:
        import capo_codebuild.types.host_kernel

        out["hostKernel"] = capo_codebuild.types.host_kernel.serialize_aws_json_1_1(
            value["host_kernel"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectEnvironment:
    out: ProjectEnvironment = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.environment_type

        out["type"] = capo_codebuild.types.environment_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("ProjectEnvironment.type required")
    if data.get("image") is not None:
        out["image"] = data["image"]
    else:
        raise DeserializationError("ProjectEnvironment.image required")
    if data.get("computeType") is not None:
        import capo_codebuild.types.compute_type

        out["compute_type"] = (
            capo_codebuild.types.compute_type.deserialize_aws_json_1_1(
                data["computeType"]
            )
        )
    else:
        raise DeserializationError("ProjectEnvironment.compute_type required")
    if data.get("computeConfiguration") is not None:
        import capo_codebuild.types.compute_configuration

        out["compute_configuration"] = (
            capo_codebuild.types.compute_configuration.deserialize_aws_json_1_1(
                data["computeConfiguration"]
            )
        )
    if data.get("fleet") is not None:
        import capo_codebuild.types.project_fleet

        out["fleet"] = capo_codebuild.types.project_fleet.deserialize_aws_json_1_1(
            data["fleet"]
        )
    if data.get("environmentVariables") is not None:
        import capo_codebuild.types.environment_variables

        out["environment_variables"] = (
            capo_codebuild.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    if data.get("privilegedMode") is not None:
        out["privileged_mode"] = data["privilegedMode"]
    if data.get("certificate") is not None:
        out["certificate"] = data["certificate"]
    if data.get("registryCredential") is not None:
        import capo_codebuild.types.registry_credential

        out["registry_credential"] = (
            capo_codebuild.types.registry_credential.deserialize_aws_json_1_1(
                data["registryCredential"]
            )
        )
    if data.get("imagePullCredentialsType") is not None:
        import capo_codebuild.types.image_pull_credentials_type

        out["image_pull_credentials_type"] = (
            capo_codebuild.types.image_pull_credentials_type.deserialize_aws_json_1_1(
                data["imagePullCredentialsType"]
            )
        )
    if data.get("dockerServer") is not None:
        import capo_codebuild.types.docker_server

        out["docker_server"] = (
            capo_codebuild.types.docker_server.deserialize_aws_json_1_1(
                data["dockerServer"]
            )
        )
    if data.get("hostKernel") is not None:
        import capo_codebuild.types.host_kernel

        out["host_kernel"] = capo_codebuild.types.host_kernel.deserialize_aws_json_1_1(
            data["hostKernel"]
        )
    return out
