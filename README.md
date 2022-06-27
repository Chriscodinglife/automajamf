# automajamf

![jamf](https://media.jamf.com/images/icons/jamf-og-image.jpg?h=600&q=80&w=600)

This is a proof of concept script that I am hoping grows into something a little more of a handy tool to quickly deploy and test, in an automated fashion, policies that need to
get created and tested in JAMF.

The goal of this is script is to take a policy, assign it to a device or a batch of machines (either physical or VM's) and then run said policy on each machine and produce an output or flag that says whether or not the test policy run was successful. 

### Run checks by running the following:

```bash
python3 -m unittest automajamf_test.py
```