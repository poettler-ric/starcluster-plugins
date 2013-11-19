from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log
from os import path

class MsmtpInstaller(ClusterSetup):
	def __init__(self):
		None

	def run(self, nodes, master, user, user_shell, volumes):
		log.info("installing msmtp on master and copying ~/.msmtprc")
		# TODO: switch to package_install - in the current release
		# package_provider is broken, so we have to stick with
		# apt_install
		#master.package_install("msmtp")
		master.apt_install("msmtp")
		master.ssh.switch_user(user)
		master.ssh.put(path.expanduser("~/.msmtprc"))
