
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {

        vector<int> result;

        if (root == NULL) {
            return result;
        }

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {

            int size = q.size();

            for (int i = 0; i < size; i++) {

                TreeNode* node = q.front();
                q.pop();

                // Last node of each level
                if (i == size - 1) {
                    result.push_back(node->val);
                }

                if (node->left != NULL) {
                    q.push(node->left);
                }

                if (node->right != NULL) {
                    q.push(node->right);
                }
            }
        }

        return result;
    }
};
