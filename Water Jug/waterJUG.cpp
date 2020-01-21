#include <bits/stdc++.h>
#define pii pair<int, int>
#define mp make_pair
using namespace std;

void BFS(int a, int b, int target)
{
    // Map is used to store the states, every
    // state is hashed to binary value to
    // indicate either that state is visited
    // before or not
    map<pii, int> m;
    bool isSolvable = false;
    vector<pii> path;

    queue<pii> q;   // queue to maintain states
    q.push({0, 0}); // Initialing with initial state

    while (!q.empty())
    {
        bool p = false;
        pii u = q.front(); // current state

        q.pop(); // pop off used state

        // if this state is already visited
        if (m[{u.first, u.second}] == 1)
            continue;

        // doesn't met jug constraints
        if ((u.first > a || u.second > b || u.first < 0 || u.second < 0))
            continue;

        // filling the vector for constructing
        // the solution path
        path.push_back({u.first, u.second});

        // marking current state as visited
        m[{u.first, u.second}] = 1;

        // if we reach solution state, put ans=1
        if (u.first == target || u.second == target)
        {
            isSolvable = true;
            if (u.first == target)
            {
                if (u.second != 0)
                    // fill final state
                    path.push_back({u.first, 0});
            }
            else
            {
                if (u.first != 0)
                    // fill final state
                    path.push_back({0, u.second});
            }

            // print the solution path
            int sz = path.size();

            for (int i = 0; i < sz; i++)
                cout << "(" << path[i].first << ", " << path[i].second << ")\n";

            break;
        }

        // if we have not reached final state
        if (u.first < 4)
        {
            q.push({a, u.second}); // fill Jug1
            // cout << u.first << "    fill a   " << u.second << endl;
        }
        if (u.second < 3)
        {
            q.push({u.first, b}); // fill Jug2
            // cout << u.first << "    fill b  " << u.second << endl;
        }
        // empty
        if (u.second > 0)
        {
            q.push({u.first, 0}); // Empty Jug2
        }
        if (u.first > 0)
        {
            q.push({0, u.second}); // Empty Jug1
        }
        // start
        int x = u.first;
        int y = u.second;
        // pour water jug2 --> jug1
        if (((x + y) > 0) && ((x + y) >= a) && (y > 0) && (x > 0))
        {
            int aa = a;
            int bb = y - (a - x);
            q.push({aa, bb});
            // cout << aa << "+++" << bb << endl;
        }
        // pour water jug1 --> jug2
        if (((x + y) > 0) && ((x + y) >= b) && (x > 0) && (y > 0))
        {

            int bb = b;
            int aa = x - (b - y);
            q.push({aa, bb});
            cout << aa << "+-+" << bb << endl;
        }
        // // (x+y,0)
        if ((0 < (x + y) && (x + y) <= a) && y >= 0)
        {
            int aa = x + y;
            int bb = 0;
            q.push({aa, bb});
            // cout << aa << " -- " << bb << endl;
        }

        // // (0,x+y)
        if ((0 < (x + y) && (x + y) <= b) && x >= 0)
        {
            int bb = x + y;
            int aa = 0;
            q.push({aa, bb});
            // cout << aa << "  " << bb << endl;
        }
        // end
    }

    // No, solution exists if ans=0
    if (!isSolvable)
        cout << "No solution";
}

// Driver code
int main()
{
    int Jug1 = 4, Jug2 = 3, target = 2;
    cout << "Path from initial state "
            "to solution state :\n";
    BFS(Jug1, Jug2, target);
    return 0;
}

// g++ -o waterJUG waterJUG.cpp && waterJUG.exe