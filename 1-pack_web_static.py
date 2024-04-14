from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        local("mkdir -p versions")

        archive_name = "web_static_{}.tgz".format(timestamp)

        local("tar -czvf versions/{} web_static".format(archive_name))

        return "versions/{}".format(archive_name)
    except Exception as e:
        print("An error occurred during archive creation:", e)
        return None
