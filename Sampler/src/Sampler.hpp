#ifndef SAMPLER_HPP
#define SAMPLER_HPP

#include "MemoryManager.hpp"
#include "Signature.hpp"
#include "CallParser.hpp"

#include <vector>
#include <map>
#include <string>

class Sampler {
    private:
        std::map<const std::string, Signature> signatures;

        MemoryManager mem;
        std::vector<CallParser> callparsers;

        std::vector<int> counters;

        template <typename T> void named_malloc(const std::vector<std::string> &tokens, std::size_t multiplicity);
        template <typename T> void named_offset(const std::vector<std::string> &tokens, std::size_t multiplicity);
        void named_free(const std::vector<std::string> &tokens);
        void add_call(const std::vector<std::string> &tokens);
        void go();

    public:
        void set_counters(const std::vector<std::string> &counters);
        void add_signature(const Signature &signature);
        void start();
};

#endif /* SAMPLER_HPP */
