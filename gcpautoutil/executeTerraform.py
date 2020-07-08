import os

from python_terraform import Terraform, IsFlagged

def removestatefile(wdir):

    if os.path.exists(wdir+r'\terraform.tfstate'):
        os.remove(wdir+r'\terraform.tfstate')
    if os.path.exists(wdir + r'\terraform.tfstate.backup'):
        os.remove(wdir + r'\terraform.tfstate.backup')
    if os.path.exists(wdir + r'\terraform.tfplan'):
        os.remove(wdir + r'\terraform.tfplan')
    # if os.path.exists(wdir + r'\terraform.tfvars'):
    #     os.remove(wdir + r'\terraform.tfvars')

def executedeployment(resource):
    """
    executing terraform commands
    :param resource: the resource getting deployed
    :return: None
    """
    wdir = 'terraform/' + resource
    tf = Terraform(working_dir=wdir)
    print resource+'>>INIT\n'
    print(tf.init())

    print resource+'>>PLAN\n'
    approve = {"auto-approve": True}
    tf.plan(no_color=IsFlagged, refresh=False, capture_output=True,out = 'output.tfplan',**approve)

    print(tf.plan())
    print(tf.apply(skip_plan=True))

    removestatefile(wdir)