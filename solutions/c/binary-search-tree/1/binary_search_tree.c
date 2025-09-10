#include "binary_search_tree.h"
#include <stdlib.h>

static node_t *insert_node(node_t *tree, int data) {
    if (tree == NULL) {
        node_t *new_node = (node_t *)malloc(sizeof(node_t));
        if (new_node == NULL) {
            return NULL; // Memory allocation failed
        }
        new_node->data = data;
        new_node->left = NULL;
        new_node->right = NULL;
        return new_node;
    }

    if (data <= tree->data) {
        tree->left = insert_node(tree->left, data);
    } else {
        tree->right = insert_node(tree->right, data);
    }
    return tree;
}

node_t *build_tree(int *tree_data, size_t tree_data_len) {
    if (tree_data_len == 0) {
        return NULL;
    }

    node_t *root = NULL;
    for (size_t i = 0; i < tree_data_len; i++) {
        root = insert_node(root, tree_data[i]);
    }
    return root;
}

void free_tree(node_t *tree) {
    if (tree == NULL) {
        return;
    }
    free_tree(tree->left);
    free_tree(tree->right);
    free(tree);
}

static size_t count_nodes(node_t *tree) {
    if (tree == NULL) {
        return 0;
    }
    return 1 + count_nodes(tree->left) + count_nodes(tree->right);
}

static int in_order_traversal(node_t *tree, int *data, int index) {
    if (tree == NULL) {
        return index;
    }
    index = in_order_traversal(tree->left, data, index);
    data[index++] = tree->data;
    index = in_order_traversal(tree->right, data, index);
    return index;
}

int *sorted_data(node_t *tree) {
    size_t count = count_nodes(tree);
    if (count == 0) {
        return NULL;
    }

    int *data = (int *)malloc(sizeof(int) * count);
    if (data == NULL) {
        return NULL; // Memory allocation failed
    }

    in_order_traversal(tree, data, 0);
    return data;
}
