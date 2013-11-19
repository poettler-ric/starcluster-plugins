from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class OpenFoamInstaller(ClusterSetup):
	def __init__(self):
		None

	def run(self, nodes, master, user, user_shell, volumes):
		for node in nodes:
			self.aptInstallOpenFoam(node)

	def aptInstallOpenFoam(self, instance):
		repository = "deb http://www.openfoam.org/download/ubuntu `lsb_release -cs` main"
		listFile = "/etc/apt/sources.list.d/openfoam.list"
		installOptions = "-y --force-yes"
		package = "openfoam222"

		log.info("installing %s on %s" % (package, instance.alias))
		
		# install the package
		instance.ssh.execute("echo %s > %s" % (repository, listFile))
		instance.ssh.execute("apt-get update")
		instance.ssh.execute("apt-get %s install %s" % (installOptions, package))

		# set the environment
		instance.ssh.execute("echo . /opt/%s/etc/bashrc >> ~/.bashrc" % package)
