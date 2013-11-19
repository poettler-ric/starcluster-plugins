from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class OpenFoamInstaller(ClusterSetup):
	def __init__(self):
		None

	def run(self, nodes, master, user, user_shell, volumes):
		package = "openfoam222"

		# install it on all nodes
		for node in nodes:
			self.aptInstallOpenFoam(node, package)

		# set the environment
		master.ssh.switch_user(user)
		master.ssh.execute("echo . /opt/%s/etc/bashrc >> ~/.bashrc" % package)

	def aptInstallOpenFoam(self, instance, package):
		repository = "deb http://www.openfoam.org/download/ubuntu `lsb_release -cs` main"
		listFile = "/etc/apt/sources.list.d/openfoam.list"

		log.info("installing %s on %s" % (package, instance.alias))
		
		# install the package
		instance.ssh.execute("echo %s > %s" % (repository, listFile))
		instance.apt_command("update")
		instance.apt_install(package)
